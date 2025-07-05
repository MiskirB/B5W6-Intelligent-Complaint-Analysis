# src/embed_and_index.py

import os
import pandas as pd
import re
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
from tqdm import tqdm


def chunk_text(text, chunk_size=300, chunk_overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - chunk_overlap
    return chunks


def load_and_chunk(csv_path):
    df = pd.read_csv(csv_path)

    chunk_data = []
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Chunking complaints"):
        chunks = chunk_text(row["cleaned_narrative"])
        for c in chunks:
            chunk_data.append({
                "complaint_id": idx,
                "product": row["Product"],
                "text": c
            })

    return pd.DataFrame(chunk_data)


def embed_texts(texts, model_name="all-MiniLM-L6-v2", batch_size=64):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True, batch_size=batch_size)
    return embeddings


def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def save_vector_store(index, metadata, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    index_path = os.path.join(save_dir, "faiss_index.index")
    metadata_path = os.path.join(save_dir, "metadata.pkl")

    faiss.write_index(index, index_path)
    with open(metadata_path, "wb") as f:
        pickle.dump(metadata, f)

    print(f"✅ Saved FAISS index to {index_path}")
    print(f"✅ Saved metadata to {metadata_path}")


def main():
    csv_path = "data/filtered_complaints.csv"
    save_dir = "vector_store"

    print("🔹 Loading and chunking...")
    chunk_df = load_and_chunk(csv_path)

    print("🔹 Embedding...")
    texts = chunk_df["text"].tolist()
    embeddings = embed_texts(texts)

    print("🔹 Building FAISS index...")
    index = build_faiss_index(embeddings)

    print("🔹 Saving vector store...")
    metadata = chunk_df.to_dict(orient="records")
    save_vector_store(index, metadata, save_dir)

    print("🎉 Task 2 complete.")


if __name__ == "__main__":
    main()
