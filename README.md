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

- `cd` to `server` directory and run `pip install -r requirements.txt`
- Run the Python file `server.py`
- In another terminal, `cd` to `client` and run `npm install`
- Run `npm run dev`
- When the app loads, enter your OpenAI API key in the provided input field

### Deployment Instructions

#### Server Deployment (Railway)

1. Create a [Railway](https://railway.app/) account
2. Install Railway CLI: `npm i -g @railway/cli`
3. Login: `railway login`
4. Create new project: `railway init`
5. Deploy: `railway up`
6. Copy your deployed server URL for client configuration

#### Client Deployment (Vercel)
1. Create a [Vercel](https://vercel.com/) account
2. Install Vercel CLI: `npm i -g vercel`
3. From the client directory:
   ```bash
   cd client
   vercel
   ```
4. Set the environment variable in Vercel:
   - VITE_SERVER_URL=https://your-railway-server-url
5. Deploy: `vercel --prod`

Your application will be live with:
- Server running on Railway (free tier includes 500 hours/month)
- Client hosted on Vercel (unlimited for static sites)
- Users provide their own OpenAI API keys
