# Autonomous Anomaly RAG Studio[cite: 7]

A fully containerized, local Retrieval-Augmented Generation (RAG) system designed for automated system log analysis and AI-powered infrastructure diagnostics. It runs completely offline using lightweight local models, ensuring your sensitive logs never leave your local environment or container.

## Tech Stack
* **Orchestration:** Docker & Docker Compose
* **CI/CD Automation:** GitHub Actions (`.github/workflows/ci-cd.yml`)
* **Frontend/Dashboard:** Streamlit
* **Vector Database:** ChromaDB (Persisted locally)
* **Embeddings:** HuggingFace `all-MiniLM-L6-v2`
* **Local LLM:** Google `flan-t5-small` via HuggingFace Pipelines

---

## Project Structure
```text
anomaly_rag_studio/
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # Automated CI/CD test and Docker build pipeline
├── app.py                # Streamlit web interface & RAG pipeline runner[cite: 7]
├── detect_anomalies.py   # Headless anomaly detection and triage script[cite: 7]
├── ingest_logs.py        # Log ingestion and vector database creation script
├── Dockerfile            # Container build instructions (Python 3.10 slim)[cite: 7]
├── docker-compose.yml    # Service orchestration and volume mounting[cite: 7]
└── chroma_db/            # Persistent vector database directory

```

---

## Getting Started

1. **Clone the repository:**

```bash
git clone [https://github.com/articlesmli/anomaly_rag_studio.git](https://github.com/articlesmli/anomaly_rag_studio.git)
cd anomaly_rag_studio

```

2. **Build and run the container:**

```bash
docker compose up --build

```

3. **Access the dashboard:**
Open your browser at **`http://localhost:8501`**

