from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 1. Sample local logs (or load from a file)
log_data = [
    "2026-09-18 10:00:01 INFO Server started successfully on port 8080",
    "2026-09-18 10:05:22 WARNING High memory usage detected: 89%",
    "2026-09-18 10:10:45 ERROR Database connection timeout on /api/v1/data",
    "2026-09-18 10:15:00 INFO User authentication successful for user_id=42"
]

# 2. Convert raw strings into LangChain Document objects
docs = [Document(page_content=log) for log in log_data]

# 3. Initialize open-source embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Create and persist Chroma vector store locally
persist_directory = "./chroma_db"
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=persist_directory
)

print(f"Successfully ingested {len(docs)} logs into ChromaDB at '{persist_directory}'!")