from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.qa_chain import get_qa_chain

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/chat")
async def chat(query: Query):
    qa = get_qa_chain()
    # Use ainvoke because FastAPI supports async
    result = await qa.ainvoke(query.question)
    return {"answer": result}
