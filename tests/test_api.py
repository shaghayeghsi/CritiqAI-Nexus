from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health():
    r=client.get("/health"); assert r.status_code==200 and r.json()["status"]=="ok"
def test_support():
    r=client.post("/api/v1/support/chat",headers={"X-Tenant-ID":"test-org"},json={"user_id":"u1","message":"I cannot access my account"})
    assert r.status_code==200 and r.json()["category"]=="account_access"
