from app.services.llm import get_llm
from app.services.prompts import RAG_PROMPT
from app.retrieval.search import search_documents

def format_sources(documents):
    sources=[]

    for document in documents:
        sources.append({
            "source":document.metadata.get("source"),
            "page": document.metadata.get("page"),
            "content":document.page_content
        })
    
    return sources

def ask_questions(question: str, k:int=3):

    documents=search_documents(
        question,k=k
    )

    if not documents:
        return{
            "answer":"i dont have enough information in the provided documents.",
            "source":[]
        }

    context="\n\n".join(
        document.page_content
        for document in documents
    )

    prompt=RAG_PROMPT.format(
        context=context,
        question=question
    )

    llm=get_llm()

    response=llm.invoke(prompt)

    return {
        "answer":response,
        "source":format_sources(documents)
    }