from app.ingestion.loader import load_pdf
from app.ingestion.chunker import split_documents
from app.retrieval.vector_store import get_vector_store

def index_document(file_path: str):
    documents=load_pdf(file_path)

    chunks=split_documents(documents)

    vector_store=get_vector_store()
    
    vector_store.add_documents(chunks)

    return len(chunks)

    