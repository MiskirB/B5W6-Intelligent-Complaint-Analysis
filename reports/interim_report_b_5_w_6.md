# 📃 Interim Report: Intelligent Complaint Analysis for Financial Services

**Challenge:** Nova AI Sprint B5W6\
**Engineer:** Miskir B.\
**Date:** July 6, 2025

---

## ✨ 1. Introduction

CrediTrust Financial, a fast-growing East African fintech, processes thousands of customer complaints monthly across its mobile-first platforms. The current process for identifying trends or issues in complaints is manual, time-consuming, and reactive. This project aims to build an internal RAG-based (Retrieval-Augmented Generation) AI tool that enables non-technical teams to query and extract insights from complaints efficiently.

This interim report documents Tasks 1 and 2, which include data cleaning, exploratory data analysis (EDA), text chunking, embedding generation, and vector index creation using FAISS.

---

## 📈 2. Business Motivation

CrediTrust's internal teams (Product, Support, Compliance) face several pain points:

- Manual review of thousands of narrative complaints
- Limited ability to query insights by product
- No real-time detection of emerging issues or fraud

Our solution aims to:

- Reduce manual triage time from days to minutes
- Empower internal teams to ask natural language questions
- Surface complaint patterns using semantic retrieval and LLM-based synthesis

---

## 🔢 3. Task 1: Exploratory Data Analysis and Preprocessing

### ▶️ Dataset Overview

- Source: CFPB Consumer Complaint Dataset
- Initial size: \~1.2M rows
- Key columns used: `Product`, `Consumer complaint narrative`, `Date received`, `Issue`

### ▶️ Product Filtering

Only 5 relevant financial products were selected for analysis:

- Credit card
- Personal loan
- Buy Now, Pay Later (BNPL)
- Savings account
- Money transfer / virtual currency

### ▶️ Narrative Cleaning

Out of the filtered records, entries with non-null complaint narratives were retained. Final cleaned dataset: **25,000+ records**

#### Cleaning Pipeline:

- Lowercased all text
- Removed special characters
- Stripped boilerplate phrases (e.g., "I am writing to...")
- Saved to: `data/filtered_complaints.csv`

### ▶️ EDA Findings

- BNPL and Credit Card have the highest complaint volume
- Word count of narratives ranges from 10 to 2000+
- Many narratives mention fraud, delays, and refund issues

---

## 🛠️ 4. Task 2: Chunking, Embedding, and Vector Store Indexing

### ▶️ Chunking Strategy

- Used a sliding window with:
  - `chunk_size = 300`
  - `chunk_overlap = 50`
- Output: ~800,000 chunks

### ▶️ Embedding Model

- Model: `all-MiniLM-L6-v2`
- Justification: Fast, GPU-optimized, and well-suited for semantic similarity tasks

### ▶️ Embedding Execution

- Platform: Google Colab (GPU runtime)
- Batch size: 64
- Execution time: ~45 minutes

### ▶️ FAISS Index Creation

- FAISS `IndexFlatL2` used for similarity search
- Vector dimension: 384
- Total vectors indexed: **800,676**

### ▶️ Metadata Handling

Each chunk was tagged with:

- Original complaint ID
- Product category
- Raw chunk text

### ▶️ Saved Files

- FAISS index: `vector_store/faiss_index.index` (~1.2GB)
- Metadata: `vector_store/metadata.pkl` (~218MB)

---

## 🫠 5. Technology Stack

- Python 3.11
- Pandas, NumPy, tqdm
- SentenceTransformers (`all-MiniLM-L6-v2`)
- FAISS (CPU)
- Google Colab (for GPU acceleration)

---

## ⚡️ 6. Challenges Faced

- Slow CPU embedding on initial runs
- FAISS index size exceeded 1.2GB requiring cloud storage
- Need to switch to Google Colab GPU to avoid runtime bottlenecks
- Git notebook metadata conflicts resolved using `nbstripout`

---

## 📏 7. Screenshots & Outputs

> **Note:** Screenshots and plots are saved in `/reports/` folder.

- Product distribution by volume
- Narrative word count histogram
- Preview of cleaned dataset
- Embedding progress via tqdm
- FAISS index and metadata summary

---

## ⏳ 8. Next Steps (Task 3 & 4 Preview)

### Task 3: RAG Retrieval Pipeline

- Implement a retrieval function to embed user query
- Fetch top-k matching chunks using FAISS
- Use LLM (via Hugging Face or OpenAI) to generate response
- Evaluate quality using 5-10 representative user questions

### Task 4: Interactive UI

- Build a Gradio or Streamlit interface
- Allow free-text user input
- Display generated answers and source chunks
- Optional: Add response streaming and filters by product

---

## 📚 Appendix

- Code: `notebooks/01_EDA_and_Cleaning_B5W6.ipynb`, `notebooks/02_chunking_embedding_indexing.ipynb`
- Cleaned Data: `data/filtered_complaints.csv`
- Vector Store: `vector_store/faiss_index.index`, `metadata.pkl`
- Scripts: `src/embed_and_index.py`

---

**Prepared by:** Miskir B.\
**GitHub Repo:** [github.com/MiskirB/B5W6-Intelligent-Complaint-Analysis](https://github.com/MiskirB/B5W6-Intelligent-Complaint-Analysis)
