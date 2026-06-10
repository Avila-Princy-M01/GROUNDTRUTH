from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.schemas.evaluation import EvaluationRequest
from app.db.models import Evaluation 
from app.db.session import SessionLocal

# Add our Head Chef import!
from app.services import evaluation_service

router = APIRouter()

def get_db():
    db = SessionLocal() 
    try:
        yield db       
    finally:
        db.close()      

@router.post("/evaluations")
def create_evaluation(request: EvaluationRequest, db: Session = Depends(get_db)):
    # The Waiter literally just hands the order to the Chef!
    new_evaluation = evaluation_service.process_new_evaluation(db, request)

    return {"message": "Saved via Clean Architecture!", "id": new_evaluation.id}

@router.get("/evaluations/{evaluation_id}")
def read_evaluation(evaluation_id: int, db: Session = Depends(get_db)):
    evaluation = db.query(Evaluation).filter(Evaluation.id == evaluation_id).first()
    return evaluation 
