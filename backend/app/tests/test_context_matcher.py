from app.ml.context_matcher import ContextMatcher

def test_perfect_match():
    context = "Python was created by Guido van Russum."
    claim = "Python was created by Guido van Russum."
    score = ContextMatcher.calculate_overlap_score(claim, context)
    assert score == 1.0

def test_hallucinated_claim():
    context = "Python was created by Guido van Russum in 1991."
    claim = "Java was invented by James Gosling in 1995."
    score = ContextMatcher.calculate_overlap_score(claim, context)
    assert score == 0.0

def test_partial_match():
    context = "PostSQL is an adavanced open-source relational database."
    claim = "PostSQL is a database developed in Germany."
    score = ContextMatcher.calculate_overlap_score(claim, context)
    # 'postsql' and 'database' match, but 'developed' and 'germany' do not.
    assert 0.0 < score < 1.0

def test_empty_inputs():
    assert ContextMatcher.calculate_overlap_score("", "some context") == 0.0
    assert ContextMatcher.calculate_overlap_score("some claim", "") == 0.0

