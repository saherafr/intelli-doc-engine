from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    tokenizer="deepset/roberta-base-squad2"
)

def answer_question(question: str, context: str) -> str:
    result = qa_pipeline(question=question, context=context)
    return result["answer"]
