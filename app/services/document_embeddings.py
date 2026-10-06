from app.ingestion.chunker import split_documents
from app.ingestion.loader import load_pdf
from app.services.embeddings import get_embedding_model

def create_embeddings(file_path:str):
    documents=load_pdf(file_path)
    chunks=split_documents(documents)

    embedding_model=get_embedding_model()
    
    texts=[chunk.page_content for chunk in chunks]

    vectors=embedding_model.embed_documents(texts)

    return chunks, vectors