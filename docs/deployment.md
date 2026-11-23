# Deployment notes
Local: install requirements, copy `.env.example` to `.env`, then run `uvicorn app.main:app --reload`.
Docker: `docker compose up --build`. Compose starts API, PostgreSQL, Qdrant, Redis, and n8n. Change development passwords before shared deployment. Before production, configure TLS, managed database/backups, authentication, authorization, webhook credentials, monitoring, and tenant isolation.
