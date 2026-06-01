from fastapi import FastAPI 
from app.api.routes import evaluations

app  = FastAPI(title="GroundTruth API")

app.include_router(evaluations.router)

@app.get("/health")
def health_check():
    return {"status": "ok", 
            "message": "GroundTruth API is running!"}

