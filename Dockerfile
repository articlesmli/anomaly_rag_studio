FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Install required packages with pinned transformers version for text2text-generation support
RUN pip install --no-cache-dir langchain-core langchain-community langchain-chroma sentence-transformers "transformers<5" torch streamlit

COPY . /app

CMD ["python3", "detect_anomalies.py"]