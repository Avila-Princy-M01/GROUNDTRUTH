from sqlalchemy.orm import Session 
from app.schemas.evaluation import EvaluationRequest
from app.db.models import Evaluation, Metric 
from app.repositories import evaluation_repo
from app.ml.claim_extractor import ClaimExtractor 
from app.ml.context_matcher import ContextMatcher

def process_new_evaluation(db:Session, request: EvaluationRequest) -> Evaluation:
    #1. Save the initial evaluation record to the database (Status: PENDING)
    saved_eval = evaluation_repo.save_evaluation(db, request)

    #2. Extract individual claims from the AI's answer
    claims = ClaimExtractor.extract_claims(request.answer)

    #If the answer was empty or had no claims, mark as completed with scoe 0 
    if not claims:
        saved_eval.status = "COMPLETED"
        db.commit()
        return saved_eval 
    
    #3. Grade each claim against the retrieved context
    claim_scores = []
    for claim in claims:
        score = ContextMatcher.calculate_overlap_score(claim, request.retrieved_context)
        claim_scores.append(score)

    #4. Calculate overall Faithfulness Score (average score converted to 0-100 integer)
    average_score = sum(claim_scores) / len(claim_scores)
    faithfulness_score = int(round(average_score * 100))

    #5. Save the calculated Metric into PostgreSQL 
    metric = Metric(score=faithfulness_score, evaluation_id=saved_eval.id)
    db.add(metric)

    #6. Update evaluation status to COMPLETED and commit changes
    saved_eval.status = "COMPLETED"
    db.commit()
    db.refresh(saved_eval)

    return saved_eval