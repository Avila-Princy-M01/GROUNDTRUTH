from sqlalchemy.orm import Session 
from app.schemas.evaluation import EvaluationRequest
from app.db.models import Evaluation 

def save_evaluation(request: EvaluationRequest, db: Session) -> Evaluation:
    #1. Map the bouncer datat to db model
    new_eval = Evaluation(
        question=request.question,
        answer=request.answer
        #we are not passing status here
        #the db will automatically inject the "PENDING" for us!
    )
 
    #2. Save it to the db
    db.add(new_eval)
    db.commit()
    db.refresh(new_eval)

    return new_eval