from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.postgres import PostgresSaver

from app.agents.tools import search_knowledge_base

from app.config import POSTGRES_URL

from app.config import GEMINI_API_KEY, MODEL


llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0,
    google_api_key=GEMINI_API_KEY
)

tools = [search_knowledge_base]

llm_with_tools = llm.bind_tools(tools)


def agent(state: MessagesState):

    system_message = SystemMessage(
        content="""
You are an enterprise knowledge assistant.

You have access to a company knowledge-base search tool.

Rules:

1. Use the knowledge-base tool when the user's question
   requires information from company documents.

2. Answer using the retrieved information.

3. Do not invent company policies or facts.

4. If the knowledge base does not contain the answer,
   clearly say that the information was not found.

5. When using retrieved information, mention the
   relevant source and page when available.

6. For general questions that do not require company
   knowledge, you may answer directly.

7. Use previous conversation messages when they are
   relevant to the current question.
"""
    )

    response = llm_with_tools.invoke(
        [system_message] + state["messages"]
    )

    return {
        "messages": [response]
    }


def create_graph(checkpointer):

    graph = StateGraph(MessagesState)

    graph.add_node("agent", agent)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "agent")

    graph.add_conditional_edges(
        "agent",
        tools_condition
    )

    graph.add_edge("tools", "agent")

    return graph.compile(
        checkpointer=checkpointer
    )