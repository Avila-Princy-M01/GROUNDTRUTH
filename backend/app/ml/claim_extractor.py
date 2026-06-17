import re

class ClaimExtractor:
    """
    Responsible for breaking a large text (like an LLM answer) into individual, testable claims.
    """

    @staticmethod
    def extract_claims(text: str) -> list[str]:
        if not text or not text.strip():
            return []

    #A simple regrex to split by ., !, or ? followed by a space
    #This is our V1 "Sentence Segmentation" approach
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    #Clean up any empty strings and strip whitespaces
        claims = [sentence.strip() for sentence in sentences if sentence.strip()]

        return claims
        
