from app.agents.graph import build_graph


graph = build_graph()


response = graph.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "How many vacation days do employees receive and how many months i can take leave if i try to use only 4 leaves per month?"
            }
        ]
    }
)


for message in response["messages"]:
    print("\n--- MESSAGE ---")
    print(message)