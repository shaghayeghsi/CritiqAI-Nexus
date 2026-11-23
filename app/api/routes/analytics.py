from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.session import get_db
from app.database.models import Ticket
from app.core.tenant import get_tenant_id
router=APIRouter(prefix="/analytics",tags=["analytics"])
@router.get("/overview")
def overview(tenant_id:str=Depends(get_tenant_id),db:Session=Depends(get_db)):
    total=db.query(func.count(Ticket.id)).filter(Ticket.tenant_id==tenant_id).scalar() or 0
    escalated=db.query(func.count(Ticket.id)).filter(Ticket.tenant_id==tenant_id,Ticket.status=="escalated").scalar() or 0
    return {"tenant_id":tenant_id,"total_tickets":total,"escalated_tickets":escalated,"resolved_tickets":total-escalated}
