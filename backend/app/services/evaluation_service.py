from sqlalchemy.orm import Session 
from app.schemas.evaluation import EvaluationRequest
from app.db.models import Evaluation 
from app.repositories import evaluation_repo

def process_new_evaluation(db:Session, request: EvaluationRequest) -> Evaluation:
    #the head chef checks the order here. if we wanted to add a spam filter or calculate the length of the question, we would write that code right here

    #once the chef is happy, they hand the verified order to the pantry worker:
    saved_eval = evaluation_repo.save_evaluation(db, request)

    return saved_eval