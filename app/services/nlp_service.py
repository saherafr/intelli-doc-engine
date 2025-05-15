from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
classifier = pipeline("zero-shot-classification")

def summarize_text(text: str, max_words=500) -> str:
    if len(text.split()) > max_words:
        text = " ".join(text.split()[:max_words])
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def classify_text(text: str) -> str:
    candidate_labels = ["resume", "invoice", "contract", "legal", "academic", "medical"]
    result = classifier(text, candidate_labels)
    return result["labels"][0]
