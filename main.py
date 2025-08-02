#from langgraph.graph import StateGraph, START, END
#from streamlit import streamlit_app
#from langchain_openai import ChatOpenAI
#from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from fastapi import UploadFile, File
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional
import os
import tempfile
from data_pipeline.injest import load_pdf, load_txt
from agent.agent import first_node

app = FastAPI(title="ContractMe API", description="API for processing documents")

class FileData(BaseModel):
    filename: str
    file_type: Optional[str] = None
    file_size: int
    content: str

@app.get("/")
def read_root():
    return {"message": "ContractMe API is running!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Process uploaded file data"""
    try:
        # Create a temporary file to save the uploaded content
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            # Process the file based on its type
            if file.filename.lower().endswith('.pdf'):
                injested_data = load_pdf(temp_file_path)
                content = "\n\n".join([doc.page_content for doc in injested_data])
            elif file.filename.lower().endswith('.txt'):
                content = load_txt(temp_file_path)
            else:
                # For other file types, try to read as text
                with open(temp_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            
            # Process with the agent
            state = first_node(content)
            
            # Clean up temporary file
            os.unlink(temp_file_path)
            
            # Example processing
            processed_data = {
                "filename": file.filename,
                "file_size": len(content),
                "status": "processed",
                "message": f"Successfully processed {file.filename}",
                "content_length": len(content),
                "content": state.model_dump_json()
            }
            
            return processed_data
            
        except Exception as e:
            # Clean up temporary file in case of error
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
            raise e
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.post("/process")
async def process_document(file: UploadFile = File(...)):
    """Alternative endpoint for document processing"""
    try:
        # Create a temporary file to save the uploaded content
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            # Process the file based on its type
            if file.filename.lower().endswith('.pdf'):
                injested_data = load_pdf(temp_file_path)
                content = "\n\n".join([doc.page_content for doc in injested_data])
            elif file.filename.lower().endswith('.txt'):
                content = load_txt(temp_file_path)
            else:
                # For other file types, try to read as text
                with open(temp_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            
            # Process with the agent
            state = first_node(content)
            
            # Clean up temporary file
            os.unlink(temp_file_path)
            
            result = {
                "filename": file.filename,
                "processing_status": "completed",
                "extracted_text_length": len(content),
                "analysis": "Document processed successfully",
                "content": state.model_dump_json()
            }
            
            return result
            
        except Exception as e:
            # Clean up temporary file in case of error
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
            raise e
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



