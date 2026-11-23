from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.rag.chunking import chunk_text
def retrieve(question,documents,top_k=3):
    passages=[]
    for doc in documents:
        for i,chunk in enumerate(chunk_text(doc.text)):
            passages.append({"document_id":doc.id,"title":doc.title,"source":doc.source,"chunk_index":i,"snippet":chunk,"tenant_id":doc.tenant_id})
    if not passages: return []
    matrix=TfidfVectorizer(stop_words="english").fit_transform([question]+[p["snippet"] for p in passages])
    scores=cosine_similarity(matrix[0:1],matrix[1:]).ravel()
    ranked=sorted(zip(scores,passages),key=lambda x:float(x[0]),reverse=True)
    return [{**p,"score":round(float(s),4)} for s,p in ranked[:top_k] if s>0]
