
# Retrieval-Augmented Generation (RAG) QA System
## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) based Question Answering system for AI research papers. The system retrieves relevant information from research papers using semantic search and generates context-aware answers using a Large Language Model (LLM).

## Features
- Research paper document processing
- Text chunking and embedding generation
- FAISS vector database
- Semantic search and retrieval
- LLM-based answer generation
- Streamlit user interface
- Source-aware responses

## Technologies Used
- Python
- LangChain
- FAISS
- Sentence Transformers
- HuggingFace
- Streamlit

## Workflow
- Load research paper PDFs
- Split documents into chunks
- Generate embeddings
- Store embeddings in FAISS
- Retrieve relevant chunks
- Generate answers using LLM
- Display results through Streamlit

## Project Summary

Developed a Retrieval-Augmented Generation (RAG) based Question Answering system using AI research papers as the knowledge source. The project preprocesses research papers, generates embeddings using Sentence Transformers, stores them in a FAISS vector database, retrieves relevant content based on user queries, and generates context-aware answers using a HuggingFace language model through a Streamlit interface.

## Project Structure

rag-research-paper-qa-system/
│
├── app.py                 # Streamlit web application
├── build_index.py         # Loads PDFs and creates FAISS vector index
├── rag_engine.py          # RAG pipeline and question-answering logic
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
├── data/
│   ├── paper1.pdf
│   ├── paper2.pdf
│   └── paper3.pdf
│
└── vector_index/
    ├── index.faiss
    └── index.pkl
