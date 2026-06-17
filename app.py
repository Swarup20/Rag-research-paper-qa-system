
import streamlit as st
from src.rag_pipeline import get_answer

st.title("RAG Based Research Paper QA System")

query = st.text_input("Ask a question from the uploaded research papers:")

if st.button("Get Answer"):
    if query:
        answer = get_answer(query)
        st.write(answer)
