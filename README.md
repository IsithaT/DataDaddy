# Data Dave

## AI-powered CSV analysis tool that provides instant insights and visualizations from your data, making data analysis accessible and efficient

![image](https://github.com/user-attachments/assets/daf85350-8e64-4cfd-ba01-7359811b4283)
![image](https://github.com/user-attachments/assets/242d4480-7b74-4edc-b8d4-a141bf963a4d)

### Notable features

- **Combats context-loss and AI hallucinations**
  - Heavily limits the data fed directly to the LLM to prevent context loss while still providing fully accurate analysis
  - Makes use of fine-tuned and prompt-engineered functions to make sure the assistant doesn't spew out random/false data
- **Accessible, code-free data analysis**
  - Upload your CSV file and get instant insights and visualizations from your prompts
  - No coding and/or Excel knowledge required!
- **Real-time data analysis**
  - Chat-based interaction allows you to quick adjust your prompts and get feedback
- **Data visualization**
  - Get visualizations of your data in the form of graphs and charts right from your dynamic prompts

### How it works

- **Function calling**
  - The LLM is given a set of fine-tuned, prompt-engineered functions that allow it to analyze the data in a way that is both accurate and contextually aware
  - It is able to choose which functions to use based on the context it is given
- **WebSockets**
  - Data is communicated between the front-end and the back-end using WebSockets, allowing for both text and image data to be sent
- **Client-server communication**
  - The front-end is built using React-TypScript, and the back-end is built using Flask
  - Through the use of WebSockets, we are able to send the message thread between the user and the AI model to the back-end for processing, and display the messages just like a text conversation
    - The message display has Markdown support, allowing for easy reading of the messages
   
### Quick dev run: 
- Add `OPENAI_API_KEY` to `.env` file in `server`
- `cd` to `server` directory and run the Python file `server.py` (will have to `pip install -r requirements.txt`)
- In another terminal, `cd` to `client` and run `npm run dev` (will have to `npm install`)
