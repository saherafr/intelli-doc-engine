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

## Backstory

I’ve always been curious about how Docker and the cloud actually work — and why every serious project uses them. Once I started exploring, I realized Docker isn’t just a developer tool — it ensures environment consistency, simplifies deployment, and makes scaling effortless. The cloud adds flexible storage, global reach, and pay-as-you-go infrastructure. I wanted to build something that brings both together in a real-world use case.

Now, why IntelliDoc?

You might say, “Can’t ChatGPT already answer questions from PDFs?” Sure — but it's trained on general internet data and shared with everyone. What if I need a private, domain-specific system, fine-tuned for internal reports, academic documents, or company policies?

That’s what IntelliDoc is built for — a foundation to power custom, secure, and intelligent document analysis at scale.
## Folder Structure

intelli-doc-engine/
│
├── app/                   # FastAPI route handlers
│   └── routes/
│
├── services/              # Core logic for S3, OCR, NLP, NER, QA
├── main.py                # App entry point
├── Dockerfile             # For containerization
├── requirements.txt       # Dependencies
├── .env.example           # Environment config template
└── README.md              # This file



## API Overview

All routes can be tested at `/docs`.

### POST /upload/

- Upload a document
- Accepts: PDF or image
- Returns: S3 URL of the uploaded file

### POST /analyze/

- Run the full pipeline (OCR → NER → Summary → QA)
- Input: S3 file path
- Returns: Extracted text, named entities, summary, and answer

## Installation

```bash
git clone https://github.com/saherafr/intelli-doc-engine.git
cd intelli-doc-engine
pip install -r requirements.txt
```
## Environment Setup

This project requires AWS credentials and configuration for uploading files to Amazon S3.
Create a .env file in the root directory based on .env.example with the following content:

AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=ca-central-1
AWS_S3_BUCKET=intellidoc-bucket
Make sure to keep this file private. It is already excluded from Git tracking via .gitignore.

## Docker Support 

You can build and run IntelliDoc Engine using Docker for an isolated, production-ready environment.

-Build the Docker image:
docker build -t intellidoc-engine .
-Run the container with your environment file:
docker run --env-file .env -p 8000:8000 intellidoc-engine
Once running, you can access the API docs at:
http://localhost:8000/docs

