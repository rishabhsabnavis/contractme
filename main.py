#from langgraph.graph import StateGraph, START, END
#from streamlit import streamlit_app
#from langchain_openai import ChatOpenAI
#from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from fastapi import UploadFile, File, Request
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional
import os
import tempfile
from agent.agent import create_venue_agent_graph
from agent.helpers import parse_twilio_webhook, generate_twiml_response

app = FastAPI(title="ContractMe API", description="API for calling venues and processing documents")




class FileData(BaseModel):
    filename: str
    file_type: Optional[str] = None
    file_size: int
    content: str





@app.get("/")
def read_root():
    return {"message": "ContractMe API is running!"}

@app.post("/voice")
async def handle_voice_webhook(request: Request):
    """Handle voice webhook"""
    return {"message": "Voice webhook received!"}

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
            
            
            # Process with the agent
            state = first_node(content)
            
            # Clean up temporary file
            os.unlink(temp_file_path)
            
            # Return processed data
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




