import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

load_dotenv()

search = DuckDuckGoSearchAPIWrapper()


@tool
def web_search(query: str) -> str:
    """Search the web and return short text results."""
    return search.run(query)


llm = ChatOpenAI(model="gpt-4o-mini")

agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt="You are a research assistant. Use web_search before you answer.",
)

question = "What is LangChain?"
result = agent.invoke({"messages": [{"role": "user", "content": question}]})
print(result["messages"][-1].content)