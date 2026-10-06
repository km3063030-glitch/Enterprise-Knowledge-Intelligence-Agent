from langchain_chroma import Chroma
from app.services.embeddings import get_embedding_model

PERSIST_DIRECTORY= "data/chroma"

def get_vector_store():
    embedding_model=get_embedding_model()
    vector_store=Chroma(
        collection_name="enterprise_documents",
        embedding_function=embedding_model,
        persist_directory=PERSIST_DIRECTORY
    )
    return vector_store