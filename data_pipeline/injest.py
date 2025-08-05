from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os
from typing import List, Dict, Any 
from dotenv import load_dotenv
from langchain.schema import Document

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


def create_or_get_chroma_collection(collection_name: str = "contracts"):
    try:
        embeddings = setup_chroma_embeddings()
        vectorstore = Chroma(persist_directory=CHROMA_PERSIST_DIR, embedding_function=embeddings, collection_name=collection_name)
        return vectorstore
    except Exception as e:
        raise Exception("Error creating or getting Chroma collection")


def add_documents_to_chroma(chunks: List[Any], collection_name: str = "contracts") -> Chroma:
    try:
        vectorstore = create_or_get_chroma_collection(collection_name)
        vectorstore.add_documents(chunks)
        vectorstore.persist()
        return vectorstore

    except Exception as e:
        raise Exception("Error adding documents to Chroma")
    


def search_chroma_collection(query: str, collection_name: str = "contracts", k: int = 5):
    try:
        vectorstore = create_or_get_chroma_collection(collection_name)
        results = vectorstore.similarity_search(query, k=k)
        return results
    except Exception as e:
        raise Exception("Error searching Chroma collection")
    

def process_pdf_with_chroma(file_path: str, collection_name: str = "contracts") -> Dict[str, Any]:
    try:
        docs = load_pdf(file_path)
        chunks = chunk_documents(docs)
        vectorstore = add_documents_to_chroma(chunks, collection_name)
        return {
            "original_docs": docs,
            "chunks": chunks,
            "vectorstore": vectorstore,
            "num_chunks": len(chunks),
            "collection_name": collection_name,
            "status": "success"
        }
    except Exception as e:
        raise Exception("Error processing PDF with Chroma")
    
def process_text_with_chroma(text: str, collection_name: str = "contracts") -> Dict[str, Any]:
    try:
        # Step 1: Create document from text
        doc = Document(page_content=text, metadata={"source": "text_input"})
        
        # Step 2: Chunk text
        chunks = chunk_documents([doc])
        
        # Step 3: Add to ChromaDB
        vectorstore = add_documents_to_chroma(chunks, collection_name)
        
        # Step 4: Return results
        return {
            "chunks": chunks,
            "num_chunks": len(chunks),
            "collection_name": collection_name,
            "status": "success"
        }
    except Exception as e:
        raise Exception("Error processing text with Chroma")
    
def clear_chroma_collection(collection_name: str = "contracts"):
    try:
        vectorstore = create_or_get_chroma_collection(collection_name)
        vectorstore._collection.delete(where={})
        return{"message": "Collection deleted successfully"}
    except Exception as e:
        raise Exception("Error clearing Chroma collection")
    

    






