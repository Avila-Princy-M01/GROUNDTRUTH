from ml.claim_extractor import ClaimExtractor

test_text = "FastAPI is a modern web framework. It is incredibly fast. Do you like it? I think it's great."

print("Original Text:")
print(test_text)
print("-" * 40)

#call your method
claims = ClaimExtractor.extract_claims(test_text)

print("Extracted Claims:")
for i, claim in enumerate(claims, 1):
    print(f"{i}. {claim}")
