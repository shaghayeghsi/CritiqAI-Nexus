import logging, httpx
from app.core.config import settings
logger=logging.getLogger(__name__)
def notify_escalation(ticket_id,tenant_id,message):
    url=settings.n8n_webhook_url.strip()
    if not url:
        logger.info("Escalation recorded; n8n not configured (ticket=%s)",ticket_id); return False
    try:
        r=httpx.post(url,json={"event":"ticket.escalated","ticket_id":ticket_id,"tenant_id":tenant_id,"message":message},timeout=5)
        r.raise_for_status(); return True
    except httpx.HTTPError:
        logger.exception("n8n notification failed for ticket %s",ticket_id); return False
