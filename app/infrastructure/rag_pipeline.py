from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from ..infrastructure.llm_client import get_llm

def build_rag_pipeline(filepath: str):
    loader = TextLoader(filepath)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever()
    llm = get_llm()
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    return chain
