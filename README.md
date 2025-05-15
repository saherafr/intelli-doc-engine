# IntelliDoc Engine

IntelliDoc is a smart document analysis backend built with FastAPI, powered by HuggingFace Transformers, and integrated with AWS S3 and Docker for scalable, production-ready deployment.

It’s not just an OCR tool — it’s a foundation for custom document intelligence, capable of summarizing content, extracting entities, and answering questions from PDFs or images.

## Features

- Upload PDFs or images
- Summarize long documents using `facebook/bart-large-cnn`
- Ask custom questions using `deepset/roberta-base-squad2`
- Extract named entities (people, places, organizations) via `dbmdz/bert-large-cased-finetuned-conll03-english`
- Built-in OCR for scanned documents using Tesseract
- Store files in Amazon S3
- Fully containerized with Docker
- Swagger UI included for easy testing at `/docs`

## Tech Stack

- Framework: FastAPI
- NLP Models: HuggingFace Transformers
- OCR: Tesseract + `pdf2image`
- Cloud Storage: AWS S3
- Deployment: Docker

## BackStory

I’ve always been curious about how Docker and the cloud actually work — and why every serious project uses them. Reading the documentation made me realize Docker isn’t just a dev tool — it ensures environment consistency, simplifies deployment, and scales beautifully. The cloud adds flexible storage, global reach, and pay-as-you-go compute. I knew I had to try them together.

Now, why IntelliDoc?

You might say: "Can’t ChatGPT already answer questions from PDFs?" Sure — but it’s trained on general internet data and shared with everyone. What if I need a private, domain-specific system, fine-tuned for my own documents, my company’s policies, or academic content?

That’s where IntelliDoc comes in — a customizable, scalable backend to build private AI document assistants for real-world use cases.

##Folder Structure

intelli-doc-engine/
│
├── app/
│   └── routes/          # FastAPI route handlers
│
├── services/            # S3, OCR, NLP, NER, QA logic
├── main.py              # App entry point
├── Dockerfile           # For containerization
├── requirements.txt     # Dependencies
├── .env.example         # Environment config template
└── README.md            # You're here!

##API Overview
--All routes can be tested at /docs.

--POST /upload/
  Upload a document
  Accepts: PDF or image
  Returns: S3 URL of the uploaded file

--POST /analyze/
  Run the full pipeline (OCR → NER → Summary → QA) on a document
  Input: S3 file path
  Returns: Extracted text, entities, summary, and answer
  
## Installation

```bash
git clone https://github.com/saherafr/intelli-doc-engine.git
cd intelli-doc-engine
pip install -r requirements.txt
## Enviroment Setup
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=ca-central-1
AWS_S3_BUCKET=intellidoc-bucket
'''
## Docker Support
docker build -t intellidoc-engine .
docker run --env-file .env -p 8000:8000 intellidoc-engine
Visit http://localhost:8000/docs to explore the API using Swagger.
