
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA

def load_vectorstore():
    loader = PyPDFLoader("data/Attention_is_All_You_Need_Study.pdf")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def get_answer(query):
    vs = load_vectorstore()
    retriever = vs.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=HuggingFaceHub(repo_id="google/flan-t5-base"),
                                     retriever=retriever)
    return qa.run(query)
