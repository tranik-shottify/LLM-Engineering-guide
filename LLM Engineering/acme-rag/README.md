# Healthcare Knowledge Assistant

RAG backend for bilingual (EN/JA) medical document retrieval. Built with FastAPI, FAISS, and sentence-transformers.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Set your API key:
```bash
export API_KEY="your-key-here"
```

Run the server:
```bash
uvicorn app.main:app --reload
```

## Environment Variables

- `API_KEY` - required for all endpoints (default: `dev-key-change-me`)
- `MODEL_NAME` - embedding model (default: `paraphrase-multilingual-MiniLM-L12-v2`)
- `INDEX_DIR` - where FAISS index gets saved (default: `./data`)

## API

### POST /ingest
Upload a .txt file. Returns detected language and doc ID.
```bash
curl -X POST http://localhost:8000/ingest \
  -H "X-API-Key: your-key" \
  -F "file=@docs/diabetes_en.txt"
```

### POST /retrieve
Query for similar documents. Returns top-k results with scores.
```bash
curl -X POST http://localhost:8000/retrieve \
  -H "X-API-Key: your-key" \
  -H "Content-Type: application/json" \
  -d '{"query": "diabetes management", "top_k": 3}'
```

### POST /generate
Get a mock LLM answer based on retrieved docs. Optional `output_language` for translation.
```bash
curl -X POST http://localhost:8000/generate \
  -H "X-API-Key: your-key" \
  -H "Content-Type: application/json" \
  -d '{"query": "diabetes treatment", "output_language": "ja"}'
```

## Docker

```bash
docker build -t acme-rag .
docker run -p 8000:8000 -e API_KEY=your-key acme-rag
```

## Tests

```bash
pytest -q
```

## Design Notes

I went with a single multilingual embedding model (`paraphrase-multilingual-MiniLM-L12-v2`) that maps both English and Japanese into the same 384-dim vector space. This means one FAISS index handles everything - a Japanese query can find English documents and vice versa without any language routing logic. The alternative would be separate indexes per language with translate-then-search, but that's more moving parts for worse results.

For scalability, `IndexFlatIP` does exact search which is fine for small doc sets but would need to be swapped to `IndexIVFFlat` or something like Qdrant once you're past ~100k documents. The sync `/ingest` endpoint would also need a task queue (Celery/Redis) for large uploads so it doesn't block the server. Documents longer than a few paragraphs would need chunking with overlap.

The services layer is split into small modules - embeddings, vector store, language detection, translation, and the mock LLM are all independent. Swapping FAISS for a managed vector DB or plugging in a real LLM is a single-file change. Auth is a FastAPI dependency so adding JWT or scopes later is straightforward. Future work would include proper citation grounding, audit logging, per-document access control, and a retrieval eval harness to measure recall and answer quality.
