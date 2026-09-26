import re

class ContextMatcher:
    """
    Responsible for checking if a claim is supported by the retrieved context.
    """

    @staticmethod
    def calculate_overlap_score(claim: str, context: str) -> float:
        if not claim or not context:
            return 0.0

        #1. Clean and tokenize claim words (lowercase, letters/numbers only)
        claim_words = set(re.findall(r'\w+', claim.lower()))
        context_words = set(re.findall(r'\w+', context.lower()))

        # Remove very common words (stop words) that don't carry real facts.
        stop_words = {"is", "was", "by", "a", "the", "it", "and", "or", "in", "on", "at", "to", "for", "of", "with", "this", "that"}
        meaningful_claim_words = claim_words - stop_words

        # If after removing stop words there's nothing left, fallback to all claim words. 
        if not meaningful_claim_words:
            meaningful_claim_words = claim_words

        if not meaningful_claim_words:
            return 0.0

        #2. Count how many meaningful claim words exist in the context
        matched_words = meaningful_claim_words.intersection(context_words)

        #3. Calculate score: matched words / total meaningful words in claim
        return round(len(matched_words) / len(meaningful_claim_words), 2)
