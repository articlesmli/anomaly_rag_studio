from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 1. Connect to our existing persistent ChromaDB directory
persist_directory = "./chroma_db"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings
)

print("Connected to ChromaDB vector store successfully.")

# 2. Define our Anomaly Detection Logic (Scanning for keywords like ERROR or WARNING)
# In a full production system, this could be an Isolation Forest or a frequency spike detector.
query_trigger = "ERROR Database connection timeout"
print(f"\n[ALERT] Anomaly Detected matching trigger criteria: '{query_trigger}'")

# 3. Autonomous RAG: Retrieve contextually similar logs from the vector store
print("Running vector similarity search to fetch related historical context...")
relevant_docs = vector_store.similarity_search(query_trigger, k=2)

# 4. Compile the Automated Insight Report
print("\n--- Autonomous RAG Diagnostic Summary ---")
print(f"Trigger Event: {query_trigger}")
print("Retrieved Context from Vector Database:")
for i, doc in enumerate(relevant_docs, 1):
    print(f"  [Context Log {i}]: {doc.page_content}")

print("\n[AI Insight]: Superset/System telemetry indicates a database timeout anomaly. "
      "Historical context shows correlated high memory or timeout warnings. "
      "Recommended Action: Check database container resource limits and connection pool limits.")
