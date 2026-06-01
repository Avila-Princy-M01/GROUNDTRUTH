from fastapi import APIRouter 
from app.schemas.evaluation import EvaluationRequest

router = APIRouter()

@router.post("/evaluations")
def create_evaluation(request: EvaluationRequest):
    return {"message": "Evaluation received!",
            "data": request}


