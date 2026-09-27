from pydantic import BaseModel 
from typing import Optional, List 

#1. What the user send TO us (Input)
class EvaluationRequest(BaseModel):
    question:str
    retrieved_context:str
    answer:str
    citations: Optional[List[str]] = None

#2. What we send BACK to the user (Output)
class EvaluationResponse(BaseModel):
    id: int 
    question: str
    answer: str
    status: str
    score: Optional[int] = None

