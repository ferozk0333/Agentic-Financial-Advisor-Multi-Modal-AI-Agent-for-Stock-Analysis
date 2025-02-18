from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai, os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


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


# Let's combine both the agents
multi_ai_agent = Agent(
    team = [finance_agent, web_search_agent],
    instructions = ["Always include sources", "Use tables to display data whereever possibe"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Should I buy NVIDIA stocks or Tesla?",stream=True)