from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from functioncalls import *
from llm import (
    load_api_key,
    initialize_client,
    create_assistant,
    create_thread,
    send_message,
    run_assistant,
    list_messages,
)
import json
import time
from PIL import Image
from io import BytesIO
import base64

# Base instructions for the assistant
BASE_INSTRUCTIONS = """You are a data analysis agent with access only to CSV headers and one sample row. Never attempt to access full data directly - use provided analysis tools instead. If a function returns an error, stop using it and try alternatives. If that doesn't work, just suggest alternatives. Always verify data types before analysis and clearly state any limitations."""

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize OpenAI client and assistant
api_key = load_api_key()
client = initialize_client(api_key)
assistant = create_assistant(client)

# Store active thread information
active_threads = {}


@socketio.on("connect")
def handle_connect():
    """
    Handles new client connections to the WebSocket server.
    Logs when a new client establishes a connection.
    """
    print("Client connected")


@socketio.on("disconnect")
def handle_disconnect():
    """
    Handles client disconnections from the WebSocket server.
    Logs when a client terminates their connection.
    """
    print("Client disconnected")


@socketio.on("join_thread")
def handle_join_thread(data):
    """
    Allows a client to join a specific chat thread room.
    Args:
        data: Dictionary containing thread_id to join
    Emits a status message confirming the room join operation.
    """
    thread_id = data.get("thread_id")
    if thread_id:
        join_room(thread_id)
        emit("status", {"msg": f"Joined thread {thread_id}"})


@socketio.on("create_thread")
def handle_create_thread():
    """
    Creates a new chat thread and adds it to active_threads.
    Creates a new room for the thread and adds the client to it.
    Emits thread creation confirmation with the new thread ID.
    """
    thread = create_thread(client)
    active_threads[thread.id] = {
        "messages": [],
        "csv_data": None,
        "headers": None,
        "data_row": None,
    }
    join_room(thread.id)
    emit("thread_created", {"thread_id": thread.id, "status": "created"})


@socketio.on("send_message")
def handle_send_message(data):
    thread_id = data.get("thread_id")
    message_content = data.get("message")

    if not thread_id or not message_content:
        emit("error", {"msg": "Missing thread_id or message"})
        return

    try:
        # Send message
        message = send_message(client, thread_id, message_content)
        emit(
            "message_sent",
            {"thread_id": thread_id, "message": message_content, "role": "user"},
            room=thread_id,
        )

        # Build context including CSV data if available
        context = BASE_INSTRUCTIONS
        if thread_id in active_threads and active_threads[thread_id]["data_row"]:
            headers = active_threads[thread_id]["headers"]
            data_row = active_threads[thread_id]["data_row"]
            context += f"\nThe CSV file contains these columns: {', '.join(headers)}."
            context += f"\nAn example row contains: {dict(zip(headers, data_row))}"
            context += "\nReference this data structure in your analysis and responses."

        # Run assistant with context
        run = client.beta.threads.runs.create(
            thread_id=thread_id, assistant_id=assistant.id, instructions=context
        )

        # Poll for run completion and handle function calls
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread_id, run_id=run.id
            )

            if run_status.status == "requires_action":
                tool_calls = run_status.required_action.submit_tool_outputs.tool_calls
                tool_outputs = []

                # Create a map of all available functions
                function_map = {
                    "calculateMean": calculateMean,
                    "calculateMedian": calculateMedian,
                    "calculateMode": calculateMode,
                    "calculateVariance": calculateVariance,
                    "calculateStandardDeviation": calculateStandardDeviation,
                    "countRows": countRows,  # Note: Using lambda since it doesn't need parameters
                    "getColumnInfo": getColumnInfo,
                    "searchValue": searchValue,
                    "searchRowDetails": searchRowDetails,  # Add the new search function
                    "bargraphToImage": bargraphToImage,  # Add the new graph function
                    "histoToImage": histoToImage,  # Add the histogram function
                    "bargraphToImage": bargraphToImage,
                    "colNameToPiechart": colNameToPiechart,  # Add the new graph function
                    "get_filtered_results_from_string": get_filtered_results_from_string,
                    "listToPiechart": listToPiechart,
                    "correlationAnalysis": correlationAnalysis,
                    "calculateMeanfromList": calculateMeanfromList,
                    "calculateMedianfromList": calculateMedianfromList,
                    "calculateModefromList": calculateModefromList,
                    "calculateVariancefromList": calculateVariancefromList,
                    "calculateStandardDeviationfromList": calculateStandardDeviationfromList,
                    "bargraphToImagefromList": bargraphToImagefromList,
                }

                # Process each tool call and collect outputs
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)

                    try:
                        if function_name in function_map:
                            print(
                                f"Executing function: {function_name} with args: {function_args}"
                            )
                            result = function_map[function_name](**function_args)
                        else:
                            result = f"Function {function_name} not implemented"

                        tool_outputs.append(
                            {"tool_call_id": tool_call.id, "output": str(result)}
                        )
                    except Exception as func_error:
                        tool_outputs.append(
                            {
                                "tool_call_id": tool_call.id,
                                "output": f"Error executing {function_name}: {str(func_error)}",
                            }
                        )

                # Submit all tool outputs together
                if tool_outputs:
                    client.beta.threads.runs.submit_tool_outputs(
                        thread_id=thread_id, run_id=run.id, tool_outputs=tool_outputs
                    )
                continue

            if run_status.status == "completed":
                break

            time.sleep(1)

        # Get and broadcast response
        messages = list_messages(client, thread_id)
        emit(
            "message_received",
            {
                "thread_id": thread_id,
                "messages": [
                    {"role": msg.role, "content": msg.content[0].text.value}
                    for msg in messages.data
                ],
            },
            room=thread_id,
        )

    except Exception as e:
        print(f"Error: {str(e)}")
        emit("error", {"msg": str(e)})


@socketio.on("clear_thread")
def handle_clear_thread(data):
    """
    Clears all messages in a specific chat thread.
    Args:
        data: Dictionary containing thread_id to clear
    Emits a status message confirming the thread clear operation.
    """
    thread_id = data.get("thread_id")
    if thread_id in active_threads:
        active_threads[thread_id]["messages"] = []
        emit(
            "thread_cleared",
            {"thread_id": thread_id, "status": "cleared"},
            room=thread_id,
        )
    else:
        emit("error", {"msg": "Invalid thread_id"})


@socketio.on("send_csv")
def handle_send_csv(data):
    thread_id = data.get("thread_id")
    csv_content = data.get("csvContent")

    try:
        # Parse CSV headers
        headers = getFirstRowFromCSV(csv_content)
        dataRow = getFirstDataRowFromCSV(csv_content)
        print(f"Processing CSV with headers: {headers}")

        # Store CSV info in thread data
        active_threads[thread_id].update(
            {"csv_data": csv_content, "headers": headers, "data_row": dataRow}
        )

        # Store CSV content globally for function calls
        setcsv(csv_content)

        # Send confirmation to client
        emit(
            "csv_processed",
            {"thread_id": thread_id, "headers": headers},
            room=thread_id,
        )

        # Build initial context with CSV information
        context = f"{BASE_INSTRUCTIONS}\n"
        context += f"The CSV file contains these columns: {', '.join(headers)}.\n"
        context += f"An example row contains: {dict(zip(headers, dataRow))}\n"
        context += "Please acknowledge this data structure and explain what kind of analysis you can perform based on the column types and content."

        message = send_message(
            client, thread_id, "I've loaded a CSV file. It is ready to be analyzed."
        )

        run = run_assistant(client, thread_id, assistant.id, context)

        # Get and send response
        messages = list_messages(client, thread_id)
        emit(
            "message_received",
            {
                "messages": [
                    {"role": msg.role, "content": msg.content[0].text.value}
                    for msg in messages.data
                ]
            },
            room=thread_id,
        )

    except Exception as e:
        print(f"CSV Processing Error: {str(e)}")
        emit("error", {"msg": f"Error processing CSV: {str(e)}"})


@socketio.on("upload_image")
def handle_upload_image(data):
    """
    Processes binary image data sent by the client and sends it back as Base64.
    Args:
        data: Dictionary containing image_data (binary Base64-encoded string).
    Emits the Base64-encoded image string to all connected clients.
    """
    image_data = data.get("image_data")

    if not image_data:
        emit("error", {"msg": "Missing image_data"})
        return

    try:
        # Decode the binary image data
        image_binary = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_binary))

        # Re-encode the image to Base64 (e.g., after resizing or processing)
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

        # Emit the image data to all connected clients
        emit(
            "image_received",
            {"image_data": encoded_image, "format": "png"},
            broadcast=True,  # This will send to all connected clients
        )
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        emit("error", {"msg": f"Error processing image: {str(e)}"})


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5001)
