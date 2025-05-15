from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.qa import router as qa_router
from app.routes.ner import router as ner_router
from app.routes.analyze import router as analyze_router
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "IntelliDoc Engine is up and running 🚀"}

# Register all routes
app.include_router(upload_router, prefix="/upload")
app.include_router(qa_router, prefix="/ask")
app.include_router(ner_router, prefix="/ner")
app.include_router(analyze_router, prefix="/analyze")
