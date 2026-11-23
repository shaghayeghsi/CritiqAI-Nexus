from datetime import datetime, timezone
from sqlalchemy import String, Text, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.session import Base
def now(): return datetime.now(timezone.utc)
class Ticket(Base):
    __tablename__="tickets"
    id: Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    tenant_id: Mapped[str]=mapped_column(String(100),index=True)
    user_id: Mapped[str]=mapped_column(String(100),default="anonymous")
    message: Mapped[str]=mapped_column(Text)
    category: Mapped[str]=mapped_column(String(50),default="general")
    status: Mapped[str]=mapped_column(String(30),default="open")
    priority: Mapped[str]=mapped_column(String(20),default="normal")
    response: Mapped[str]=mapped_column(Text,default="")
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now)
class KnowledgeDocument(Base):
    __tablename__="knowledge_documents"
    id: Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    tenant_id: Mapped[str]=mapped_column(String(100),index=True)
    title: Mapped[str]=mapped_column(String(250))
    source: Mapped[str]=mapped_column(String(500),default="manual")
    text: Mapped[str]=mapped_column(Text)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now)
