import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Page Config
st.set_page_config(page_title="Anomaly RAG Studio", page_icon="🔍", layout="centered")

st.title("🔍 Autonomous Anomaly RAG Studio")
st.markdown("Query your local vector database of system logs and get local LLM-powered diagnostics.")

# Now the cache decorator will work because 'st' is defined
@st.cache_resource
def load_rag_components():
    persist_directory = "./chroma_db"
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    
    model_id = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=64,
        do_sample=False,
        repetition_penalty=2.5
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    return vector_store, llm

with st.spinner("Loading local embeddings and LLM into memory..."):
    vector_store, llm = load_rag_components()

st.success("System ready!")

# User Input Form
query = st.text_input("Enter log error or trigger search:", value="ERROR Database connection timeout")

if st.button("Run Diagnostic"):
    with st.spinner("Searching vector database and generating reasoning..."):
        # Retrieve Context
        relevant_docs = vector_store.similarity_search(query, k=2)
        context_text = "\n".join([doc.page_content for doc in relevant_docs])
        
        # Display Context
        st.subheader("Retrieved Context Logs")
        for i, doc in enumerate(relevant_docs, 1):
            st.code(doc.page_content, language="text")
            
        # Few-shot Prompt
        prompt = (
            f"Task: Provide a root cause and fix.\n"
            f"Log: 2026-09-18 10:10:45 ERROR Database connection timeout on /api/v1/data\n"
            f"Fix: Check database service health, review network security groups, and increase connection timeout thresholds.\n\n"
            f"Task: Provide a root cause and fix.\n"
            f"Log: {context_text}\n"
            f"Fix:"
        )
        
        response = llm.invoke(prompt)
        
        # Display Output
        st.subheader("Autonomous RAG Diagnostic Summary")
        st.info(response.strip())