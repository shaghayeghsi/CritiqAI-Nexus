from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.database.models import Ticket
from app.core.tenant import get_tenant_id
from app.agents.support_graph import run_support_workflow
from app.services.notifications import notify_escalation
router=APIRouter(prefix="/support",tags=["support"])
class ChatRequest(BaseModel):
    user_id: str="anonymous"
    message: str=Field(min_length=3,max_length=5000)
@router.post("/chat")
def chat(payload:ChatRequest,tenant_id:str=Depends(get_tenant_id),db:Session=Depends(get_db)):
    result=run_support_workflow(payload.message,tenant_id)
    ticket=Ticket(tenant_id=tenant_id,user_id=payload.user_id,message=payload.message,
      category=result["category"],status="escalated" if result["escalate"] else "resolved",
      priority=result["priority"],response=result["answer"])
    db.add(ticket); db.commit(); db.refresh(ticket)
    if result["escalate"]: notify_escalation(ticket.id,tenant_id,payload.message)
    return {"ticket_id":ticket.id,**result}
