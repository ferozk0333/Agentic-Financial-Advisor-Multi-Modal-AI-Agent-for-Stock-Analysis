import openai
from phi.agent import Agent
from phi.model.groq import Groq
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os
import phi
from phi.playground import Playground, serve_playground_app

# Load environment variables
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")


# Copy the individual agents 
# Let's create our first agent - Web Search Agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for information",
    model = Groq(id = "deepseek-r1-distill-qwen-32b"),
    tools = [DuckDuckGo()],
    instructions= ["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Let's create our second agent - Financial Agent
finance_agent = Agent(
    name = "Financial Search Agent",
    model = Groq(id = "deepseek-r1-distill-qwen-32b"),
    tools=[YFinanceTools(stock_price=True, company_info=True, key_financial_ratios = True, company_news = True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Use tables to display data where possible."],

)


# Let's create the playground for chatbot

app = Playground(
    agents= [finance_agent, web_search_agent],
).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)       # playground -> is hte file name and app -> is from where my program starts