# Agentic-Financial-Advisor: Multi-Modal AI Agent for Stock Analysis

An autonomous AI-powered financial analysis tool using **multi-modal agents, LLMs (DistilBERT, Grok), YFinance API, DuckDuckGo Search, and FastAPI**. This project integrates **Agentic AI** principles to provide **real-time stock analysis, news insights, and financial recommendations**.

---

### Agentic AI Pipeline

1. **User Input**: The user queries the AI about stock performance.  
2. **Web Search Agent**: Fetches the latest financial news using **DuckDuckGo API**.  
3. **Finance Analysis Agent**: Retrieves **real-time stock data** via **YFinance API**.  
4. **Multi-Agent Coordination**: Aggregates and processes the data using **LLMs (Grok, DistilBERT)**.  
5. **AI-Powered Insights**: Returns a **summary, sentiment analysis, and investment recommendations**.  
6. **FastAPI UI**: The results are displayed in an interactive chatbot interface.  


---


## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/ferozk0333/Agentic-Financial-Advisor.git
cd Agentic-Financial-Advisor
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure API Keys
Create a `.env` file in the project directory:
```ini
GROK_API_KEY=your_grok_key_here
PHIDATA_API_KEY=your_data_key_here
```

### Run the Financial Agent
```bash
python financial_agent.py
```

### Start the Chatbot Playground
```bash
python playground.py
```
Access the playground at **http://localhost:7777/**.

---


## Example Usage

```bash
python financial_agent.py
```

Example Query:
```arduino
"Summarize the latest news and stock performance for NVIDIA (NVDA)"
```

AI Response:
```latex
"NVDA stock is up 3.5% today. Analysts recommend a STRONG BUY due to recent AI advancements. 
Latest news: NVIDIA partners with Tesla for AI-powered car systems."
```


