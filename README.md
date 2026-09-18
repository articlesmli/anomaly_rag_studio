# Autonomous Anomaly RAG Studio

A fully containerized, local Retrieval-Augmented Generation (RAG) system designed for automated system log analysis and AI-powered infrastructure diagnostics. It runs completely offline using lightweight local models, ensuring your sensitive logs never leave your local environment or container.

## Tech Stack
* **Orchestration:** Docker & Docker Compose
* **Frontend/Dashboard:** Streamlit
* **Vector Database:** ChromaDB (Persisted locally)
* **Embeddings:** HuggingFace `all-MiniLM-L6-v2`
* **Local LLM:** Google `flan-t5-small` via HuggingFace Pipelines

---

## Project Structure
```text
anomaly_rag_studio/
├── app.py                # Streamlit web interface & RAG pipeline runner
├── detect_anomalies.py   # Headless anomaly detection and triage script
├── Dockerfile            # Container build instructions (Python 3.10 slim)
├── docker-compose.yml    # Service orchestration and volume mounting
└── chroma_db/            # Persistent vector database directory
