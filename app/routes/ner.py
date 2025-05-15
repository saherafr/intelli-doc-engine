from fastapi import APIRouter, Form
from app.services.ner_service import extract_entities

router = APIRouter()

@router.post("/")
async def ner(text: str = Form(...)):
    entities = extract_entities(text)
    return {
        "entities": entities
    }
