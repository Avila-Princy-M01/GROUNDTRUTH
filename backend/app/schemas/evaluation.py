from pydantic import BaseModel 
from typing import Optional, List 

class EvaluationRequest(BaseModel):
    question:str
    retrieved_context:str
    answer:str
    citations: Optional[List[str]] = None
