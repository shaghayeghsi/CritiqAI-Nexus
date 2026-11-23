from fastapi import FastAPI
from app.core.config import settings
from app.database.session import init_db
from app.api.routes import support, knowledge, learning, analytics

app = FastAPI(title=settings.app_name, version="0.1.0")
@app.on_event("startup")
def startup(): init_db()
@app.get("/health", tags=["system"])
def health(): return {"status":"ok","service":"critiqai-nexus","provider":settings.llm_provider}
app.include_router(support.router, prefix=settings.api_v1_prefix)
app.include_router(knowledge.router, prefix=settings.api_v1_prefix)
app.include_router(learning.router, prefix=settings.api_v1_prefix)
app.include_router(analytics.router, prefix=settings.api_v1_prefix)
