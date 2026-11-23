# Architecture
FastAPI exposes the product APIs. LangGraph orchestrates the in-app support flow. The current mock provider classifies and responds deterministically. SQLAlchemy stores tickets and knowledge documents with tenant IDs. The knowledge endpoint filters records by tenant before lexical ranking. n8n is reserved for external business actions; Qdrant and Redis are provisioned in Compose as integration points.

**Security boundary:** the current `X-Tenant-ID` header is a development context selector, not identity or authorization. Production requires authentication, membership checks, PostgreSQL row-level security, audit logging, rate limits, and secret management.
