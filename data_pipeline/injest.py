from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os
from typing import List, Dict, Any 
from dotenv import load_dotenv
#Config Stuff
CHROMA_PERSIST_DIR = "./chroma_db"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


load_dotenv()


def load_pdf(file_path: str) -> str:
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs

def load_docx(file_path: str) -> str: 
    loader = Docx2txtLoader(file_path)
    docs = loader.load()
    return docs


def load_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    


def chunk_documents(docs: List[Any], chunk_size: int = CHUNK_SIZE, chunk_overlap: int= CHUNK_OVERLAP) -> List[Any]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
    chunks = text_splitter.split_documents(docs)
    return chunks


def setup_chroma_embeddings():
    try:
        embeddings = OpenAIEmbeddings()
        return embeddings
    except Exception as e:
        raise Exception("Error setting up embeddings on Chroma")


#def create_or_get_chroma_collection(collection_name: str = "contracts"):