from fastapi import APIRouter, Form
from app.services.qa_service import answer_question

router = APIRouter()

@router.post("/")
async def ask(question: str = Form(...), filename: str = Form(...)):
    context_path = f"uploads/context/{filename}.txt"
    with open(context_path, "r", encoding="utf-8") as f:
        context = f.read()

    answer = answer_question(question, context)
    return {
        "question": question,
        "answer": answer
    }
