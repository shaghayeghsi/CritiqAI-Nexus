from app.rag.chunking import chunk_text
from app.learning.argumentation import analyze_argument
def test_chunking():
    assert chunk_text("one two three four five six",3,1)==["one two three","three four five","five six"]
def test_argument_score():
    result=analyze_argument("Remote learning improves access for adults","It helps because schedules are flexible.","A published study with a representative sample.")
    assert 0<=result["rubric_score"]<=100 and "feedback" in result
