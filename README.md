# Data Dave

## AI-powered CSV analysis tool that provides instant insights and visualizations from your data, making data analysis accessible and efficient

### Notable Features

- **Accessible data analysis**
  - Upload your CSV file and get instant insights and visualizations from your prompts
  - No coding and/or Excel functions required!
- **Real-time data analysis**
  - Chat-based interaction allows you to quick adjust your prompts and get feedback
- **Context-loss combating**
  - Heavily Limits the data fed directly to the LLM to prevent context loss while still providing fully accurate analysis
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
    - 