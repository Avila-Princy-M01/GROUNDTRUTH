from fastapi import status
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.schemas.evaluation import EvaluationRequest, EvaluationResponse
from app.db.models import Evaluation, Metric
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

@router.post("/evaluations", response_model=EvaluationResponse)
def create_evaluation(request: EvaluationRequest, db: Session = Depends(get_db)):
    #1. The Waiter literally just hands the order to the Chef!
    eval_result = evaluation_service.process_new_evaluation(db, request)

    #2. Fetch the newly computed metric score
    metric = db.query(Metric).filter(Metric.evaluation_id == eval_result.id).first()
    score = metric.score if metric else None

    #3. Return the full response matching EvaluationResponse
    return EvaluationResponse(
        id=eval_result.id,
        question=eval_result.question,
        answer=eval_result.answer,
        status=eval_result.status,
        score=score
    )

@router.get("/evaluations/{evaluation_id}", response_model=EvaluationResponse)
def read_evaluation(evaluation_id: int, db: Session = Depends(get_db)):
    #1. Search for the evaluation in the database 
    evaluation = db.query(Evaluation).filter(Evaluation.id == evaluation_id).first()

    #2. If it does not exist, return a 404 error
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation not found")

    #3. Look up the score
    metric = db.query(Metric).filter(Metric.evaluation_id == evaluation_id).first()
    score = metric.score if metric else None

    #4. Return the clean response
    return EvaluationResponse(
        id=evaluation_id,
        question=evaluation.question,
        answer=evaluation.answer,
        status=evaluation.status,
        score=score
    )

@router.get("/evaluations", response_model=list[EvaluationResponse])
def list_evaluations(db: Session = Depends(get_db)):
    #1. Fetch all evaluations from the database
    evaluations = db.query(Evaluation).all()

    #2. Build the list of response items with their scores
    results = []
    for evaluation in evaluations:
        metric = db.query(Metric).filter(Metric.evaluation_id == evaluation.id).first()
        score = metric.score if metric else None

        results.append(
            EvaluationResponse(
                id=evaluation.id,
                question=evaluation.question,
                answer=evaluation.answer,
                status=evaluation.status,
                score=score
            )
        )
    return results