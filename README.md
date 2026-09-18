# Autonomous RAG & Anomaly Insight Engine 

A containerized, intelligent observability pipeline that ingests system logs, indexes them into a local vector store, executes automated anomaly detection, and triggers context-aware RAG-based diagnostic summaries.

---

## Architectural Workflow

```text
[ Raw System Logs ] 
       │
       ▼
[ Ingestion Pipeline (`ingest_logs.py`) ] ──> [ HuggingFace Embeddings (`all-MiniLM-L6-v2`) ]
                                                       │
                                                       ▼
[ Persistent ChromaDB Volume (`./chroma_db`) ] <───────┘
       │
       ▼
[ Anomaly Detector & RAG Engine (`detect_anomalies.py`) ] ──> [ Contextual Diagnostic Report ]

```

---

## Core Tech Stack

* **Containerization**: Docker & Docker Compose V2
* **Vector Database**: ChromaDB (Embedded & Persistent via Docker Volumes)
* **Orchestration Framework**: LangChain (`langchain-core`, `langchain-community`, `langchain-chroma`)
* **Embedding Model**: HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
* **Runtime**: Python 3.10-slim

---

## Project Structure

```text
anomaly_rag_studio/
├── chroma_db/            # Persistent vector database storage volume
├── Dockerfile            # Container definition and package dependencies
├── docker-compose.yml    # Service orchestration and volume mapping
├── ingest_logs.py        # Log ingestion and vector indexing script
├── detect_anomalies.py   # Anomaly trigger and RAG diagnostic engine
└── README.md             # Project documentation

```

---

## Configuration Files

### `Dockerfile`

```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

RUN pip install --no-cache-dir langchain-core langchain-community langchain-chroma sentence-transformers

COPY . /app

CMD ["python3", "detect_anomalies.py"]

```

### `docker-compose.yml`

```yaml
version: '3.8'

services:
  anomaly_engine:
    build: .
    container_name: anomaly_rag_engine
    volumes:
      - ./chroma_db:/app/chroma_db
      - ./:/app
    environment:
      - PYTHONUNBUFFERED=1

```

---

## Execution Guide

### Prerequisites

* Docker and Docker Compose installed on your host machine.

### Step 1: Ingest and Index Logs

To parse raw system logs and build the vector embeddings in ChromaDB:

1. Temporarily set your `Dockerfile` CMD to run ingestion: `CMD ["python3", "ingest_logs.py"]`
2. Run the container:
```bash
docker compose up --build

```


*Expected Output:* `Successfully ingested 4 logs into ChromaDB at './chroma_db'!`

### Step 2: Run Autonomous Anomaly Detection & RAG

To scan for system anomalies and retrieve historical vector context:

1. Ensure your `Dockerfile` CMD is set to: `CMD ["python3", "detect_anomalies.py"]`
2. Run the container:
```bash
docker compose up --build

```



---

## Sample Diagnostic Output

```text
Connected to ChromaDB vector store successfully.

[ALERT] Anomaly Detected matching trigger criteria: 'ERROR Database connection timeout'
Running vector similarity search to fetch related historical context...

--- Autonomous RAG Diagnostic Summary ---
Trigger Event: ERROR Database connection timeout
Retrieved Context from Vector Database:
  [Context Log 1]: 2026-09-18 10:10:45 ERROR Database connection timeout on /api/v1/data
  [Context Log 2]: 2026-09-18 10:10:45 ERROR Database connection timeout on /api/v1/data

[AI Insight]: Superset/System telemetry indicates a database timeout anomaly. Historical context shows correlated high memory or timeout warnings. Recommended Action: Check database container resource limits and connection pool limits.

```

```

---

### How to Update Your Local File and Push:
1. Overwrite your local `README.md` file with the exact text above.
2. Run these git commands in your terminal:
   ```bash
   git add README.md
   git commit -m "Enhance README with precise architecture, configuration, and execution docs"
   git push -u origin main
