# Autonomous RAG and Anomaly Insight Engine

A containerized, intelligent observability pipeline that ingests system logs, indexes them into a local vector store, runs automated anomaly detection, and triggers context-aware RAG-based diagnostic summaries.

## Overview
Modern applications generate massive volumes of log data. Traditional monitoring relies on rigid threshold alerts that lack context. This project demonstrates an autonomous RAG workflow to bridge that gap:
1. **Ingest & Embed**: Parses raw logs and embeds them using open-source sentence transformers.
2. **Persistent Vector Storage**: Stores embeddings in a local ChromaDB instance managed via Docker volumes.
3. **Autonomous Detection**: Identifies critical anomalies (e.g., database timeouts, error spikes).
4. **Diagnostic RAG**: Automatically queries historical vector context to compile plain-English AI insights and mitigation recommendations.

---

## Core Tech Stack
* **Orchestration**: Docker & Docker Compose
* **Vector Store**: ChromaDB (Embedded & Persistent)
* **Orchestration Framework**: LangChain (`langchain-core`, `langchain-chroma`)
* **Embedding Model**: HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
* **Runtime**: Python 3.10 (Slim)

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
