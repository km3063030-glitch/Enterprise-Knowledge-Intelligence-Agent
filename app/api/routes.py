from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path
import shutil

from app.retrieval.index_documents import index_document
# from app.services.rag import ask_questions
from app.agents.service import ask_agent 

from app.services.logger import logger


router=APIRouter()

DOCUMENT_DIRECTORY=Path("data/document")
DOCUMENT_DIRECTORY.mkdir(parents=True,exist_ok=True)

# class ChatRequest(BaseModel):
#     question:str
#     thread_id: str
#     # k:int=3

class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=2000
    )

    thread_id: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

MAX_FILE_SIZE = 10 * 1024 * 1024

@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File size exceeds the 10 MB limit."
        )

    file_path = DOCUMENTS_DIRECTORY / file.filename

    with file_path.open("wb") as buffer:
        buffer.write(contents)

    # chunk_count = index_document(
    #     str(file_path)
    # )
    logger.info(
    "Uploading document: %s",
    file.filename
    )

    chunk_count = index_document(
        str(file_path)
    )

    logger.info(
        "Document indexed successfully: %s (%s chunks)",
        file.filename,
        chunk_count
    )

    return {
        "message": "Document uploaded and indexed successfully",
        "filename": file.filename,
        "chunks_indexed": chunk_count
    }

@router.post("/chat")
def chat(request: ChatRequest):

    logger.info(
        "Chat request received for thread: %s",
        request.thread_id
    )

    result = ask_agent(
        question=request.question,
        thread_id=request.thread_id
    )

    logger.info(
        "Chat request completed for thread: %s",
        request.thread_id
    )

    return result