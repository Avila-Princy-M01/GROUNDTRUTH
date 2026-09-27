from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base, Metric
from app.schemas.evaluation import EvaluationRequest
from app.services.evaluation_service import process_new_evaluation

#1. Setup a lightweight in-memory SQLite database just for fast automated testing
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_full_evaluation_flow():
    #Create the tables in our test DB
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    try:
        #2. Prepare a realistic RAG input
        request = EvaluationRequest(
            question="What is FastAPI?",
            retrieved_context="FastAPI is a modern, fast web framework for building APIs with Python.",
            answer="FastAPI is a modern web framework for building APIs."
        )

        #3. Hand the order to the Chef
        result = process_new_evaluation(db, request)

        #4. Verify the Chef completed the job
        assert result.id is not None
        assert result.status == "COMPLETED"

        #5. Verify the Metric score was calculated and saved in the DB
        saved_metric = db.query(Metric).filter(Metric.evaluation_id == result.id).first()
        assert saved_metric is not None
        assert saved_metric.score > 70 #Should be a very high faithfulness score!

    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
            