from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.schemas.evaluation import EvaluationRequest
from app.db.models import Evaluation 
from app.db.session import SessionLocal

router = APIRouter()

#our dependency injection function
def get_db():
    db = SessionLocal() 
    try:
        yield db       #this tells to hand the db session to the route and freze the function till the route is finished
    finally:
        db.close()      #unfreeze and run to clean up the session

@router.post("/evaluations")
def create_evaluation(request: EvaluationRequest, db: Session = Depends(get_db)):
    #1. convert the strict pydantic bouncer data into an sqlalchemy db row
    new_evaluation = Evaluation(
        question=request.question,
        answer=request.answer
    )
 
    #2. Throw it into the db and hit save!
    db.add(new_evaluation)
    db.commit()
    db.refresh(new_evaluation)
    
    return {"message": "Saved to PostgreSQL", "id": new_evaluation.id}

@router.get("/evaluations/{evaluation_id}")
def read_evaluation(evaluation_id: int, db: Session = Depends(get_db)):
    #ask the db to find the row where the ID matched the one requeted
    evaluation = db.query(Evaluation).filter(Evaluation.id == evaluation_id).first()
    return evaluation 