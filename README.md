# 🧠 Intelligent Complaint Analysis for Financial Services

**Author:** Miskir B.  
**Challenge:** KAIM B5W6 Intelligent Complaint Analysis for Financial Services
**Date:** July 8, 2025  
**Project:** RAG-powered Complaint QA Chatbot for CrediTrust

---

## 🚀 Introduction

CrediTrust Financial, a fast-growing East African fintech company, serves over 500,000 users with services like credit cards, loans, BNPL, savings, and money transfers. To manage thousands of monthly customer complaints, this project implements a **Retrieval-Augmented Generation (RAG)** chatbot that allows internal teams to query complaint data in plain English.

---

## 📊 Business Motivation

| Department         | Pain Point                                      |
| ------------------ | ----------------------------------------------- |
| Customer Support   | Overwhelmed by volume of complaints             |
| Product Management | No fast way to track dominant issues            |
| Compliance         | Reacts too late to fraud or repeat violations   |
| Executive          | No visibility into product-specific pain points |

Our RAG solution empowers:

- ✅ Real-time insight detection
- ✅ Natural-language querying
- ✅ Faster trend identification

---

## 🧹 Task 1: EDA and Cleaning

- Dataset: CFPB Consumer Complaints (~9.6M rows)
- Focused Products: Credit Cards, Personal Loans, BNPL, Savings, Money Transfers
- Cleaned Dataset: 25,000+ records with valid narratives
- Key Steps:
  - Lowercased text
  - Removed special characters and boilerplate
  - Saved to `data/filtered_complaints.csv`
- Insights: BNPL and Credit Card dominate; frequent issues include fraud and refund delays

---

## 🔗 Task 2: Chunking, Embedding & Indexing

- Chunking:
  - Strategy: RecursiveCharacterTextSplitter
  - Chunk Size: 300 | Overlap: 50
  - Output: ~800,000 chunks
- Embedding:
  - Model: `all-MiniLM-L6-v2`
  - Platform: Google Colab
- Indexing:
  - Vector Store: FAISS (`IndexFlatL2`)
  - Metadata: complaint ID, product, chunk text
  - Saved to `vector_store/faiss_index.index`, `metadata.pkl`

---

## 🧠 Task 3: RAG Pipeline & Evaluation

- Retrieval: Top-5 chunks via FAISS
- Generation: Prompted LLM with context + question
- Prompt Template:

```
You are a financial analyst assistant for CrediTrust.
Your task is to answer questions about customer complaints.
Use the following retrieved complaint excerpts to formulate your answer.
If the context doesn't contain the answer, state that you don't have enough information.
```

- Evaluation:

| Question                      | Score | Summary            |
| ----------------------------- | ----- | ------------------ |
| Refund delays in credit cards | 4     | Grounded but vague |
| BNPL issues                   | 3     | Abstract           |
| Unauthorized savings access   | 5     | Accurate           |
| Virtual currency concerns     | 4     | Good summary       |
| Double charge refunds         | 5     | Direct and clear   |

---

## 💬 Task 4: Interactive App

- Framework: Gradio
- Features:
  - Natural language input
  - Answer + source chunks display
  - Clear button
- Live App: [Gradio Deployment](https://d73b91a15b4b8115a2.gradio.live/)

---

## 📉 Challenges & Fixes

| Challenge                | Fix             |
| ------------------------ | --------------- |
| Large FAISS Index        | Cloud storage   |
| Colab GPU limits         | Batch embedding |
| Hallucinated LLM answers | Prompt tuning   |

---

## 📁 Deliverables

- GitHub: [MiskirB/B5W6-Intelligent-Complaint-Analysis](https://github.com/MiskirB/B5W6-Intelligent-Complaint-Analysis)
- Cleaned Data: `data/filtered_complaints.csv`
- Vector Index: `vector_store/faiss_index.index`
- Notebooks:
  - `01_EDA_and_Cleaning_B5W6.ipynb`
  - `02_chunking_embedding_indexing.ipynb`
  - `03_rag_retrieval_pipeline.ipynb`
  - `04_interactive_chat_interface.ipynb`
- App: `app.py`

---

## 🧭 Next Steps

- Add product/date filters
- Enable CSV/PDF export
- Multilingual support
- Deploy on Hugging Face Space

---

## 🎓 Learnings

- Practical use of vector DBs and semantic search
- Prompt engineering for context-grounded QA
- Importance of source visibility for trust
