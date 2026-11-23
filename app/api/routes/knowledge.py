from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.database.models import KnowledgeDocument
from app.core.tenant import get_tenant_id
from app.rag.retrieval import retrieve
router=APIRouter(prefix="/knowledge",tags=["knowledge"])
class IngestRequest(BaseModel):
    title:str=Field(min_length=1,max_length=250)
    text:str=Field(min_length=20,max_length=50000)
    source:str="manual"
class AskRequest(BaseModel):
    question:str=Field(min_length=3,max_length=3000)
    top_k:int=Field(default=3,ge=1,le=10)
@router.post("/ingest")
def ingest(payload:IngestRequest,tenant_id:str=Depends(get_tenant_id),db:Session=Depends(get_db)):
    doc=KnowledgeDocument(tenant_id=tenant_id,title=payload.title,text=payload.text,source=payload.source)
    db.add(doc); db.commit(); db.refresh(doc)
    return {"document_id":doc.id,"tenant_id":tenant_id,"status":"ingested"}
@router.post("/ask")
def ask(payload:AskRequest,tenant_id:str=Depends(get_tenant_id),db:Session=Depends(get_db)):
    docs=db.query(KnowledgeDocument).filter(KnowledgeDocument.tenant_id==tenant_id).all()
    results=retrieve(payload.question,docs,payload.top_k)
    if not results:
        return {"answer":"No supporting information was found in this organization's knowledge base. Please contact support.","sources":[],"grounded":False}
    excerpts=" ".join(x["snippet"] for x in results)
    return {"answer":"Relevant information found in the organization's documents: "+excerpts[:1600],
            "sources":results,"grounded":True}
