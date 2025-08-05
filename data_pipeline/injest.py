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
    


