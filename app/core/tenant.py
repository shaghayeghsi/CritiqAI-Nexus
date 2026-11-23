from fastapi import Header, HTTPException
def get_tenant_id(x_tenant_id: str = Header(default="demo-tenant", alias="X-Tenant-ID")):
    value=x_tenant_id.strip()
    if not value or len(value)>100: raise HTTPException(400,"Invalid tenant identifier")
    return value
