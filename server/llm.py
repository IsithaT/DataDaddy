from openai import OpenAI
import os
from dotenv import load_dotenv

def load_api_key():
    """Load the OpenAI API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set.")
    return api_key

def initialize_client(api_key):
    """Initialize the OpenAI client with the provided API key."""
    return OpenAI(api_key=api_key)

def create_assistant(client):
    """Create an assistant with the specified parameters."""
    return client.beta.assistants.create(
        name="Data Helper",
        instructions="You are a smart data bot, help the user analyse data",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4o",
    )

def create_thread(client):
    """Create a new thread."""
    return client.beta.threads.create()

def send_message(client, thread_id, content):
    """Send a message to the specified thread."""
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )

def run_assistant(client, thread_id, assistant_id, instructions):
    """Run the assistant and poll for the result."""
    return client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions=instructions
    )

def list_messages(client, thread_id):
    """List messages in the specified thread."""
    return client.beta.threads.messages.list(thread_id=thread_id)

def main():
    api_key = load_api_key()
    client = initialize_client(api_key)
    assistant = create_assistant(client)
    thread = create_thread(client)
    send_message(client, thread.id, "I need to solve the equation `3x + 11 = 14`. Can you help me?")
    run = run_assistant(client, thread.id, assistant.id, "Please address the user as Jane Doe. The user has a premium account.")
    
    if run.status == 'completed':
        messages = list_messages(client, thread.id)
        print(messages)
    else:
        print(run.status)

if __name__ == "__main__":
    main()