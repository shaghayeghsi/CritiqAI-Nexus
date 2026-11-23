from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.core.tenant import get_tenant_id
from app.learning.argumentation import analyze_argument
router=APIRouter(prefix="/learning",tags=["learning"])
class ArgumentRequest(BaseModel):
    claim:str=Field(min_length=5,max_length=2000)
    argument:str=Field(min_length=10,max_length=5000)
    evidence:str=Field(default="",max_length=5000)
@router.post("/analyze")
def analyze(payload:ArgumentRequest,tenant_id:str=Depends(get_tenant_id)):
    return {"tenant_id":tenant_id,**analyze_argument(payload.claim,payload.argument,payload.evidence)}
