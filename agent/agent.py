# Core Agent Logic, Nodes, and Graph Setup
# This file will contain:
# - Agent class/implementation
# - Processing nodes
# - LangGraph workflow
# - State management
import logging
import os
from typing import Any, Dict, List, TypedDict
import langgraph 
from pydantic import BaseModel, Optional
from langgraph.graph import END, START, StateGraph, Graph
from langchain_perplexity import PerplexityChat
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from data_pipeline import process_file_with_chroma, process_text_with_chroma
import json

# Load environment variables
load_dotenv()

# Initialize Perplexity API with GPT-5


# Voice Agent Functions



class OverallState(BaseModel):

    #Voice conversation state
    utterance: str = ""
    answer: str = ""
    call_sid = Optional[str] = None
    history = List[str] = []


    #Conversation Flow
    current_step: str = "greeting"
    intent: str = "unknown"



    #Context for RAG
    context: List[str] = []
    relevant_docs =  List[Document] = []


   
    metadata: Optional[dict] = None

   
    contract_analysis: str = ""
    contract_summary: str = ""
    contract_recommendations: str = ""

    #Venue data
    venue_name: str = ""
    query_type: str = "" #'availability, pricing, contract, general




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








def create_venue_agent_graph() -> StateGraph:
    """Agent Workflow"""
    workflow = StateGraph(state_type=OverallState)

    workflow.add_node("Retrieve Venue Context", retrieve_venue_context)
    workflow.add_node("Generate RAG Response", generate_rag_response)
    workflow.add_node("Classify Intent", classify_intent)








