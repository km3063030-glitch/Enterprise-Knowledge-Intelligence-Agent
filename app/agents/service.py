from app.agents.graph import create_graph
from langgraph.checkpoint.postgres import PostgresSaver
import os
from dotenv import load_dotenv


load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL")


checkpointer_context = PostgresSaver.from_conn_string(
    POSTGRES_URL
)

checkpointer = checkpointer_context.__enter__()

checkpointer.setup()

graph = create_graph(checkpointer)


def ask_agent(question: str, thread_id: str):

    response = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    )

    messages = response["messages"]

    final_message = messages[-1]

    sources = []

    for message in messages:

        if getattr(message, "type", None) == "tool":

            content = message.content

            lines = content.splitlines()

            current_source = None
            current_page = None

            for line in lines:

                line = line.strip()

                if line.startswith("SOURCE:"):
                    current_source = line.replace(
                        "SOURCE:",
                        ""
                    ).strip()

                elif line.startswith("PAGE:"):
                    current_page = line.replace(
                        "PAGE:",
                        ""
                    ).strip()

                if current_source and current_page:

                    sources.append(
                        {
                            "document": current_source,
                            "page": current_page
                        }
                    )

                    current_source = None
                    current_page = None

    return {
        "answer": final_message.content,
        "sources": sources
    }