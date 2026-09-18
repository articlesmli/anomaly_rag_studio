FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Install modern modular langchain packages
RUN pip install --no-cache-dir langchain-core langchain-community langchain-chroma sentence-transformers

COPY . /app

CMD ["python3", "detect_anomalies.py"]