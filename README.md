# Data Dave: AI-Powered CSV Analysis

Data Dave is your AI assistant for analyzing CSV files - no coding or Excel expertise required! Simply upload your CSV and ask questions in plain English to get instant insights and visualizations.

![Data Dave Interface](https://github.com/user-attachments/assets/daf85350-8e64-4cfd-ba01-7359811b4283)

## 🚀 Getting Started

1. Visit [Data Dave](https://datadave.colemanlai.com)
2. Get your [OpenAI API key](https://platform.openai.com/api-keys)
3. Upload your CSV file
4. Start asking questions!

## 💡 Example Questions

- "What's the average value in column X?"
- "Create a bar graph showing the distribution of Y"
- "Find any correlations between columns A and B"
- "Show me a pie chart of categories in column Z"
- "What are the top 5 values in column N?"

## ✨ Features

### Combats AI Context Loss and Hallucinations

- Heavily limits the data fed directly to the LLM to prevent context loss while still providing fully accurate analysis
- Makes use of fine-tuned and prompt-engineered functions to make sure the assistant doesn't spew out random/false data
- Maintains conversation context for follow-up questions

### Powerful Visualizations

- Bar graphs
- Pie charts
- Histograms
- Correlation plots
- Custom charts based on your needs

### User-Friendly Interface

- Chat-based interaction
- Real-time responses
- Markdown support for clear explanations
- Direct visualizations in chat

### Privacy & Security

- Your data stays in your browser
- API key transmitted securely via WebSocket
- No data permanently stored on servers

## 🛠️ Local Development

To run Data Dave locally:

1. Clone the repository
2. Set up the server:
   ```bash
   cd server
   pip install -r requirements.txt
   python server.py
   ```
3. Set up the client:
   ```bash
   cd client
   npm install
   npm run dev
   ```
4. Open the provided local URL
5. Enter your OpenAI API key to begin

## 📝 Contributing

We welcome contributions! 

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
