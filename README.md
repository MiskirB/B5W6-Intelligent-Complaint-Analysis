# 🧠 Intelligent Complaint Analysis for Financial Services

**Challenge:** Nova AI Sprint B5W6  
**Engineer:** Miskir B.  
**Status:** 🟢 In Progress (Tasks 1–2 Completed)

---

## 🔍 Project Overview

This project builds a Retrieval-Augmented Generation (RAG) pipeline for analyzing customer complaint narratives submitted to the Consumer Financial Protection Bureau (CFPB). The goal is to enable CrediTrust Financial’s non-technical teams to ask natural language questions and retrieve meaningful insights using semantic search and LLMs.

---

## 🚀 Features Implemented (Interim)

### ✅ Task 1: EDA & Cleaning

- Loaded full CFPB dataset (~9.6M rows)
- Filtered 5 key financial products
- Cleaned and processed over 25,000 narrative complaints
- Visualized:
  - Product distribution
  - Narrative word count
- Output saved to: `data/filtered_complaints.csv`

### ✅ Task 2: Chunking, Embedding & Indexing

- Used `all-MiniLM-L6-v2` for embedding 800,000+ text chunks
- Built FAISS vector index (`IndexFlatL2`)
- Saved:
  - `vector_store/faiss_index.index` (~1.2GB)
  - `vector_store/metadata.pkl` (~218MB)

---

## 📁 Directory Structure

├── data/ # Cleaned complaint dataset
├── notebooks/ # Jupyter notebooks (EDA, chunking)
│ ├── 01_EDA_and_Cleaning_B5W6.ipynb
│ └── 02_chunking_embedding_indexing.ipynb
├── reports/ # Visuals (PNG plots)
├── src/ # Custom scripts (e.g., indexing)
├── app/ # Will contain Gradio/Streamlit UI
├── vector_store/ # FAISS index and metadata
├── requirements.txt
└── README.md

---

## 📊 Visualizations

- `reports/product_distribution.png`
- `reports/narrative_wordcount.png`

---

## 🛠️ Tech Stack

- Python 3.11
- Pandas, NumPy, tqdm
- SentenceTransformers (`all-MiniLM-L6-v2`)
- FAISS (CPU)
- Google Colab (GPU-accelerated for embeddings)

---

## 📌 Next Steps

- 🧪 **Task 3:** Implement RAG retrieval pipeline (FAISS + LLM)
- 🖥️ **Task 4:** Build an interactive app with Gradio or Streamlit
- 🧾 **Final Report:** Complete and publish with evaluation results

---

## 📎 References

- CFPB Consumer Complaint Database: [consumerfinance.gov/data-research](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- Sentence-Transformers: [huggingface.co/sentence-transformers](https://huggingface.co/sentence-transformers)

---

## 🧑‍💻 Author

**Miskir B.**  
📁 GitHub Repo: [github.com/MiskirB/B5W6-Intelligent-Complaint-Analysis](https://github.com/MiskirB/B5W6-Intelligent-Complaint-Analysis)
