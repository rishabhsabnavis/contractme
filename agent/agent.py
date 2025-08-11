# Core Agent Logic, Nodes, and Graph Setup
# This file will contain:
# - Agent class/implementation
# - Processing nodes
# - LangGraph workflow
# - State management
import logging
from typing import Any, Dict, List, TypedDict
import langgraph 
from pydantic import BaseModel, Optional
from langgraph.graph import END, START, StateGraph, Graph

#from data_pipeline()



class OverallState(BaseModel):
    context: List[str]
    answer: str
    utterance: str
    history: List[str]
    call_sid: Optional[str]
    metadata: Optional[dict]












