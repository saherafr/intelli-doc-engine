from transformers import pipeline

ner_pipeline = pipeline("ner", grouped_entities=True)

def extract_entities(text: str):
    raw_entities = ner_pipeline(text)
    parsed_entities = []

    for ent in raw_entities:
        parsed_entities.append({
            "entity_group": ent["entity_group"],
            "word": ent["word"],
            "score": float(ent["score"])  # ✅ convert numpy to float
        })

    return parsed_entities
