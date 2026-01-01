import os
from fastapi import APIRouter, UploadFile, File
from app.rag.loader import load_document
from app.rag.splitter import split_docs
from app.rag.vector_store import save_vector_store

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    docs = load_document(file_path)
    chunks = split_docs(docs)
    save_vector_store(chunks)

    return {"message": "Document uploaded and indexed successfully"}
