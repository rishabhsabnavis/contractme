import langgraph

from dotenv import load_dotenv
from pydantic import BaseModel

class State(BaseModel):
    contract_text: str = ""
    contract_summary: str = ""
    contract_analysis: str = ""
    contract_recommendations: str = ""
    contract_questions: str = ""
    contract_answers: str = ""
    contract_issues: str = ""
    contract_suggestions: str = ""

    