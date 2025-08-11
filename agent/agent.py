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
    context: List[str] = []
    answer: str = ""
    utterance: str = ""
    history: List[str] = []
    call_sid: Optional[str] = None
    metadata: Optional[dict] = None
    current_step: str = "greeting"
    contract_analysis: str = ""
    contract_summary: str = ""
    contract_recommendations: str = ""


def first_node(state: OverallState) -> OverallState:
    """First node in the workflow that receives context and learns from vector database"""
    return state










