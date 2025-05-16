from fastapi import FastAPI
from app.routes.upload import router as upload_router
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI(
    title="IntelliDoc Engine",
    description="Document analysis API with OCR, QA, NER, and summary",
    version="1.0.0"
)


# Include routes
app.include_router(upload_router, prefix="")

# Run the server (Render-compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
