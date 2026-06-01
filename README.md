# GroundTruth: RAG Evaluation System

## The Problem
When developers build AI chatbots that read documents (Retrieval-Augmented Generation), the AI often hallucinates or ignores the source documents. Developers need an automated way to grade the AI's answers to see if they are trustworthy.

## 4-Week MVP Scope
This project is a Minimum Viable Product (MVP) designed to evaluate RAG systems. It currently includes:
- **Ingestion API:** Accepts a question, the retrieved context, and the AI's answer.
- **Evaluation Engine:** Grades the answer for Faithfulness (no hallucinations) and Attribution (used the context).
- **Storage:** PostgreSQL database to save evaluation results.
- **Dashboard:** A Next.js frontend to view reliability scores and trends.

### Non-Goals (Not in MVP)
- No complex background job queues (Redis/Celery)
- No advanced Vector Databases (Qdrant)
- No user authentication or multi-tenant support
- No alert systems (Email/Slack)
