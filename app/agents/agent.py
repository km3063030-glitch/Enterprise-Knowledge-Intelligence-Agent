from langchain_google_genai import ChatGoogleGenerativeAI

from app.agents.tools import search_knowledge_base

llm= ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)

tools=[
    search_knowledge_base
]

llm_with_tools=llm.bind_tools(tools)