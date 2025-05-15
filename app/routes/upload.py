from fastapi import APIRouter, File, UploadFile
import os, shutil

from app.services.ocr_service import extract_text_from_pdf, extract_text_from_image
from app.services.nlp_service import summarize_text, classify_text
from app.services.s3_service import upload_file_to_s3

router = APIRouter()

# Local directories
UPLOAD_DIR = "uploads"
CONTEXT_DIR = os.path.join(UPLOAD_DIR, "context")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CONTEXT_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    # === Step 1: Save uploaded file locally ===
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # === Step 2: OCR text extraction ===
    if file.filename.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(file_path)
    else:
        extracted_text = extract_text_from_image(file_path)

    # === Step 3: NLP tasks ===
    summary = summarize_text(extracted_text)
    classification = classify_text(extracted_text)

    # === Step 4: Save extracted context locally ===
    context_path = os.path.join(CONTEXT_DIR, f"{file.filename}.txt")
    with open(context_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    # === Step 5: Upload both file and context to S3 ===
    s3_file_url = upload_file_to_s3(file_path, f"uploads/{file.filename}")
    s3_context_url = upload_file_to_s3(context_path, f"context/{file.filename}.txt")

    # === Step 6: Return result ===
    return {
        "filename": file.filename,
        "summary": summary,
        "classification": classification,
        "raw_text_snippet": extracted_text[:300] + "...",
        "s3_file_url": s3_file_url,
        "s3_context_url": s3_context_url
    }
