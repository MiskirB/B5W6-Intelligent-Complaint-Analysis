# src/rag_pipeline.py

import faiss
import pickle
import numpy as np
import textwrap
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# === Load vector store ===
INDEX_PATH = "vector_store/faiss_index.index"
META_PATH = "vector_store/metadata.pkl"

index = faiss.read_index(INDEX_PATH)
with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

# === Retriever ===
def retrieve_similar_chunks(query, top_k=5):
    query_emb = model.encode([query])[0].astype("float32")
    D, I = index.search(np.array([query_emb]), top_k)
    results = []
    for i, idx in enumerate(I[0]):
        entry = metadata[idx]
        results.append({
            "rank": i + 1,
            "product": entry.get("product", "N/A"),
            "text": entry.get("text", entry.get("chunk", ""))
        })
    return results

# === Prompt Template ===
def format_prompt(chunks, question):
    context = "\n".join(f"- {c['text']}" for c in chunks)
    return (
        f"You are a financial analyst assistant for CrediTrust. Your task is to answer questions about customer complaints.\n"
        f"Use the following retrieved complaint excerpts to formulate your answer. If the context doesn't contain the answer, say so.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n"
        f"Answer:"
    )

# === Generator ===
def load_generator(model_name="mistralai/Mistral-7B-Instruct-v0.1", device="cpu"):
    return pipeline("text-generation", model=model_name, tokenizer=model_name, device=device)

generator = load_generator()

def generate_response(prompt):
    output = generator(prompt, max_new_tokens=300, do_sample=False)[0]['generated_text']
    return output.split("Answer:")[-1].strip()
