from fastapi import APIRouter, Form
from app.services.ocr_service import extract_text_from_pdf
from app.services.nlp_service import summarize_text, classify_text
from app.services.qa_service import answer_question
from app.services.ner_service import extract_entities

router = APIRouter()

@router.post("/")
async def analyze(filename: str = Form(...), question: str = Form("What is this document about?")):
    context_path = f"uploads/context/{filename}.txt"
    with open(context_path, "r", encoding="utf-8") as f:
        text = f.read()

    summary = summarize_text(text)
    classification = classify_text(text)
    answer = answer_question(question, text)
    entities = extract_entities(text)

    return {
        "filename": filename,
        "summary": summary,
        "classification": classification,
        "answer": {
            "question": question,
            "answer": answer
        },
        "entities": entities
    }
