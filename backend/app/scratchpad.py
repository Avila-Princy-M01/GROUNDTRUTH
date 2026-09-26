from ml.claim_extractor import ClaimExtractor
from ml.context_matcher import ContextMatcher

#1. The Ground Truth source document
reference_context = """
FastAPI is a modern, fast (high performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.
It is based on standard Python type hints.
It was created by Sebastian Ramirez in 2018.
"""

#2. An AI-generated answer containing both facts and a hallucination
ai_answer = "FastAPI is a modern web framewok. It was invented in 1850 by Thomas Edison."

print("1. Extracting CLAIMS from AI ANSWER...")
claims = ClaimExtractor.extract_claims(ai_answer)

print("\n2. Evaluating each CLAIM against CONTEXT...")
for index, claim in enumerate(claims, 1):
    score = ContextMatcher.calculate_overlap_score(claim, reference_context)
    verdict = "SUPPORTED" if score >= 0.5 else "HALLUCINATED"

    print(f"\nClaim {index}: '{claim}'")
    print(f"Evidence score: {score} -> {verdict}")
    