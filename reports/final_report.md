# 🧠 Intelligent Complaint Analysis for Financial Services

**Author:** Miskir B.  
**Challenge:** Nova AI Sprint B5W6  
**Date:** July 8, 2025

---

## 🚀 Introduction

CrediTrust Financial is a fast-growing fintech company operating across East Africa. With over **500,000 active users**, it offers digital financial services including:

- Credit Cards
- Personal Loans
- Buy Now, Pay Later (BNPL)
- Savings Accounts
- Money Transfers

However, CrediTrust receives **thousands of customer complaints** monthly across email, in-app channels, and regulatory portals. Product managers like Asha from the BNPL team spend hours manually reviewing this feedback.

To solve this, we developed a **Retrieval-Augmented Generation (RAG)** chatbot system. This system transforms unstructured narratives into actionable insights in real time. It allows internal users to ask natural-language questions and get synthesized, source-backed answers instantly.

---

## 📊 Business Motivation

| Department         | Pain Point                                   |
| ------------------ | -------------------------------------------- |
| Customer Support   | Overwhelmed by complaint volumes             |
| Product Management | No fast way to identify issue patterns       |
| Compliance         | Reacts too late to violations or fraud       |
| Executives         | Limited visibility into customer pain points |

### Project Goals:

- ⏱️ Reduce complaint triage time from days to minutes
- 🧠 Empower non-technical users with natural-language QA
- 🔍 Enable real-time detection of complaint trends

---

## 🧹 Task 1: Exploratory Data Analysis (EDA) & Preprocessing

### Dataset Overview

- Source: **CFPB Complaint Dataset** (~9.6 million rows)
- Focused on: Credit Cards, Personal Loans, BNPL, Savings Accounts, Money Transfers

### Cleaning Pipeline

- Filtered non-null narratives only
- Lowercased all text
- Removed special characters and boilerplate phrases
- Final size: **25,000+ records**
- Output: `data/filtered_complaints.csv`

### EDA Insights

- BNPL and Credit Card complaints dominate
- Narrative lengths: 10–2000+ words
- Common themes: fraud, refund delays, double charges, account closure confusion

---

## 🔗 Task 2: Text Chunking, Embedding, and Vector Indexing

### Chunking Strategy

- LangChain's RecursiveCharacterTextSplitter
- `chunk_size = 300`, `chunk_overlap = 50`
- Output: ~800,000 chunks

### Embedding Model

- Model: `all-MiniLM-L6-v2`
- Platform: Google Colab GPU
- Batch size: 64, Execution time: ~45 minutes

### Vector Index

- FAISS index (`IndexFlatL2`), Vector dim: 384
- Metadata: complaint ID, product, chunk text
- Files: `faiss_index.index`, `metadata.pkl`

---

## 🧠 Task 3: RAG Pipeline Implementation and Evaluation

### Pipeline Flow

1. Retrieve top-5 chunks from FAISS
2. Prompt template with question + context
3. Generate answer using LLM
4. Return response + top sources

### Prompt Template

```
You are a financial analyst assistant for CrediTrust.
Your task is to answer questions about customer complaints.
Use the following retrieved complaint excerpts to formulate your answer.
If the context doesn't contain the answer, state that you don't have enough information.
```

### Evaluation Table

| Question                      | Summary                             | Score | Notes                        |
| ----------------------------- | ----------------------------------- | ----- | ---------------------------- |
| Refund delays on credit cards | Charges process faster than refunds | 4     | Clear context, phrasing weak |
| BNPL issues                   | Customer support gaps               | 3     | Too abstract                 |
| Savings fraud                 | Hacked accounts, wire fraud         | 5     | Accurate                     |
| Virtual currency concerns     | Regulatory risk, Coinbase issues    | 4     | Concise                      |
| Double charges                | Merchant doesn’t refund             | 5     | Strong context match         |

---

## 💬 Task 4: Interactive Gradio Chatbot UI

### Features

- Natural language input
- AI-generated answer
- Source chunk display
- "Clear" button to reset
- Optional: streaming answers

### Live App

[Gradio Link](https://d73b91a15b4b8115a2.gradio.live/)

### Screenshot

![Gradio UI Screenshot](assets/gradio_ui_1.png)

---

## 📉 Challenges Faced

| Challenge          | Resolution              |
| ------------------ | ----------------------- |
| Large FAISS index  | Offloaded to cloud      |
| GPU session limits | Batched embeddings      |
| Hallucinations     | Refined prompt          |
| UI clarity         | Added source visibility |

---

## ✅ Final Deliverables

- GitHub Repo: https://github.com/MiskirB/B5W6-Intelligent-Complaint-Analysis
- Data: `filtered_complaints.csv`
- Vector DB: `faiss_index.index`, `metadata.pkl`
- Notebooks: `01_EDA_and_Cleaning_B5W6.ipynb`, `02_chunking_embedding_indexing.ipynb`, `03_rag_retrieval_pipeline.ipynb`, `04_interactive_chat_interface.ipynb`
- App: `app.py`

---

## 🧭 What’s Next?

- Add filtering by product and date
- CSV/PDF export of insights
- Swahili/Amharic multilingual support
- Hugging Face deployment

---

## 🎓 Learnings

- Real-world RAG systems can bridge the gap between LLMs and structured insights
- Good chunking and prompt design are essential
- Gradio enables lightweight UIs for internal stakeholders
