from langchain_core.tools import tool

from app.retrieval.search import search_documents


@tool
def search_knowledge_base(query: str) -> str:
    """
    Search the enterprise knowledge base for information
    relevant to the user's question.

    Returns relevant document content together with
    source filename and page number.
    """

    documents = search_documents(
        query=query,
        k=3
    )

    if not documents:
        return "No relevant information was found in the knowledge base."

    results = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "unknown"
        )

        page = document.metadata.get(
            "page",
            "unknown"
        )

        content = document.page_content

        results.append(
            f"""SOURCE: {source}

            PAGE: {page}

            CONTENT:{content}
            """
        )

    return "\n".join(results)