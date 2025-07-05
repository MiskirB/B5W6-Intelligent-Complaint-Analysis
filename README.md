# B5W5 - Intelligent Complaint Analysis for Financial Services

This project is part of the Nova July 2025 Challenge. It implements an AI-powered internal tool for CrediTrust Financial to analyze customer complaints across Credit Cards, BNPL, Savings, Money Transfers, and Personal Loans.

## 📌 Objectives

- Build a RAG-based chatbot using consumer complaint data
- Enable internal teams to ask plain-English questions and get grounded answers
- Reduce the time to identify complaint trends from days to minutes

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- FAISS or ChromaDB
- SentenceTransformers
- LangChain or HuggingFace Transformers
- Gradio or Streamlit

## 📁 Project Structure

├── app/ # Chatbot UI (Gradio/Streamlit)
├── data/ # Raw and cleaned complaint data
├── notebooks/ # EDA and experimental code
├── reports/ # Interim and final write-ups
├── src/ # Core logic for RAG, embeddings, retrieval
├── vector_store/ # Stored FAISS/ChromaDB index
├── README.md
├── .gitignore
└── requirements.txt
