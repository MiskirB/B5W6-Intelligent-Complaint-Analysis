import streamlit as st
import faiss
import pickle
import numpy as np
import textwrap
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# -----------------------------------
# 🔄 Load index, metadata, models
# -----------------------------------
@st.cache_resource
def load_resources():
    INDEX_PATH = "vector_store/faiss_index.index"
    META_PATH = "vector_store/metadata.pkl"

    # Load FAISS index
    index = faiss.read_index(INDEX_PATH)

    # Load metadata
    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)

    # Embedding model
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")

    # Text generation model (fallback to smaller if memory limited)
    generator = pipeline("text-generation", model="gpt2", max_new_tokens=200)

    return index, metadata, embed_model, generator

# Load once
index, metadata, embed_model, generator = load_resources()

# -----------------------------------
# 🔍 Retrieve top-k similar chunks
# -----------------------------------
def retrieve_similar_chunks(query, top_k=5):
    query_emb = embed_model.encode([query])[0].astype("float32")
    D, I = index.search(np.array([query_emb]), top_k)

    results = []
    for i, idx in enumerate(I[0]):
        entry = metadata[idx]
        results.append({
            "rank": i + 1,
            "product": entry.get("product", "N/A"),
            "text": entry.get("text") or entry.get("chunk", "")
        })
    return results

# -----------------------------------
# 🧠 Prompt Engineering
# -----------------------------------
def format_prompt(chunks, query):
    context = "\n\n".join([f"- {c['text']}" for c in chunks])
    return f"""You are a financial analyst assistant for CrediTrust. Your task is to answer questions about customer complaints.
Use the following retrieved complaint excerpts to formulate your answer.
If the context doesn't contain the answer, state that you don't have enough information.

Context:
{context}

Question: {query}
Answer:"""

def generate_response(prompt):
    result = generator(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    return result[0]['generated_text'].split("Answer:")[-1].strip()

# -----------------------------------
# 🖥️ Streamlit UI
# -----------------------------------
st.set_page_config(page_title="CrediTrust Complaint Assistant", page_icon="💬")
st.title("💬 CrediTrust Complaint Q&A Assistant")
st.markdown("Ask any question related to financial complaints. The system uses a vector search engine and a language model to provide answers.")

query = st.text_input("💬 Enter your question:")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("🔍 Searching and generating answer..."):
            chunks = retrieve_similar_chunks(query)
            prompt = format_prompt(chunks, query)
            response = generate_response(prompt)

            st.subheader("📌 Answer")
            st.write(response)

            st.subheader("📚 Sources")
            for c in chunks:
                st.markdown(f"**🔹 Product:** {c['product']}")
                st.code(textwrap.fill(c['text'], width=100), language="text")

if st.button("Clear"):
    st.experimental_rerun()
