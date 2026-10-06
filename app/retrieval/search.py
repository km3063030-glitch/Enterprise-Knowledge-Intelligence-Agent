from app.retrieval.vector_store import get_vector_store

def search_documents(query: str,k:int =3,score_threshold:float=1.0):

    vector_store=get_vector_store()

    results=vector_store.similarity_search_with_score(
        query,
        k=k
    )

    filtered_results=[
        document
        for document, score in results
        if score<=score_threshold
    ]
    
    return filtered_results