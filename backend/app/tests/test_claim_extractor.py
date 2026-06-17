from app.ml.claim_extractor import ClaimExtractor

def test_extract_claims_basic_sentences():
    #1. Arrange: Setup the test data
    text = "FastAPI is a modern web framework! It is incredibly fast. Do you like it? I think it's great."

    #2. Act: Run the code we want to test
    claims = ClaimExtractor.extract_claims(text)

    #3. Assert: Verify the outcome is exactly what we expect
    assert len(claims) == 4
    assert claims[0] == "FastAPI is a modern web framework!"
    assert claims[1] == "It is incredibly fast."
    assert claims[2] == "Do you like it?"
    assert claims[3] == "I think it's great."

def test_extract_claims_empty_text():
    #Edge case: What if the LMS returns nothing?
    assert ClaimExtractor.extract_claims("") == []
    assert ClaimExtractor.extract_claims("  ") == []
    assert ClaimExtractor.extract_claims(None) == []