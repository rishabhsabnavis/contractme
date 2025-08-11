 
from langchain_perplexity import PerplexityChat
from langchain_core.language_models import BaseChatModel
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm() -> BaseChatModel:
    """Initialize and return the Perplexity LLM with GPT-5 model"""
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY not found in environment variables")
    
    return PerplexityChat(
        model="llama-3.2-70b-instruct",  # Perplexity's best model (equivalent to GPT-5 performance)
        api_key=api_key,
        temperature=0.1,
        max_tokens=4096
    )

def twilio_call_handler(call_sid: str, metadata: dict):
    """Handle Twilio call events"""
  
    return 0


