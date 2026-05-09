from fastapi import FastAPI
from app.routers import ingest, retrieve, generate

app = FastAPI(title="Acme Healthcare RAG", version="0.1.0")

app.include_router(ingest.router)
app.include_router(retrieve.router)
app.include_router(generate.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
