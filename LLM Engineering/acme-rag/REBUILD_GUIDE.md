# Rebuild Guide: Healthcare Knowledge Assistant

Build the project from scratch, step by step.

---

## Step 0: Project Setup

Use Python 3.11.

```
py -3.11 -m venv .venv       # Windows
# python3.11 -m venv .venv   # Linux/Mac

.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # Linux/Mac
```

Create folders and empty `__init__.py` files:

```
acme-rag/
  app/
    __init__.py
    routers/
      __init__.py
    services/
      __init__.py
  tests/
    __init__.py
  docs/
```

Create `requirements.txt`:

```
fastapi
uvicorn[standard]
pydantic
python-multipart
sentence-transformers
faiss-cpu
langdetect
transformers
torch
sacremoses
sentencepiece
pytest
httpx
ruff
```

Then install:

```
pip install -r requirements.txt
```

---

## Step 1: Settings (app/settings.py)

```python
import os
from pathlib import Path

API_KEY = os.environ.get("API_KEY", "TANVIR RAHMAN ANIK")
MODEL_NAME = os.environ.get(
    "MODEL_NAME",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
)
INDEX_DIR = Path(os.environ.get("INDEX_DIR", "./data"))
INDEX_DIR.mkdir(exist_ok=True)
EMBED_DIM = 384
```

**Your choices:**
- Rename `API_KEY` to `KEY` or `SECRET`
- Change default API key to your name
- Change `./data` to `./index` or `./storage`

---

## Step 2: Auth (app/auth.py)

```python
import secrets
from fastapi import Header, HTTPException, status
from app.settings import API_KEY


def verify_key(x_api_key: str = Header(None)):
    if not x_api_key or not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
```

**Your choices:**
- Rename function to `check_api_key` or `require_key`
- Change the error detail message
- Use `403` instead of `401` (both are acceptable)

---

## Step 3: Pydantic Models (app/models.py)

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

Language = Literal["en", "ja"]


class IngestResponse(BaseModel):
    id: str
    language: Language
    num_chunks: int
    source: str


class RetrieveRequest(BaseModel):
    query: str = Field(..., min_length=1)
    top_k: int = 3


class RetrievedDoc(BaseModel):
    id: str
    text: str
    score: float
    language: str
    source: str


class RetrieveResponse(BaseModel):
    query_language: Language
    results: List[RetrievedDoc]


class GenerateRequest(BaseModel):
    query: str = Field(..., min_length=1)
    output_language: Optional[Language] = None


class GenerateResponse(BaseModel):
    query_language: Language
    output_language: Language
    answer: str
    sources: List[dict]
```

**Your choices:**
- Rename `Language` alias to `Lang` or remove it and use `Literal["en", "ja"]` inline
- Rename `RetrievedDoc` to `SearchResult` or `DocResult`
- Reorder fields within each model
- Change `top_k` default to `5` instead of `3`

---

## Step 4: Embedder (app/services/embedder.py)

```python
from sentence_transformers import SentenceTransformer
from app.settings import MODEL_NAME

_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def encode(texts):
    if isinstance(texts, str):
        texts = [texts]
    vecs = get_model().encode(texts, normalize_embeddings=True)
    return vecs.astype("float32")
```

**Why normalize?** FAISS `IndexFlatIP` computes dot product. Dot product of two unit-length vectors = cosine similarity. So normalizing lets us use the fast inner-product index for cosine search.

**Your choices:**
- Rename `_model` to `_embedder` or `_cached`
- Rename `get_model` to `load_model` or `init_model`
- Rename `encode` to `embed` or `vectorize`
- Rename `vecs` to `embeddings` or `vectors`

---

## Step 5: Vector Store (app/services/store.py)

```python
import json
import faiss
from app.settings import INDEX_DIR, EMBED_DIM


class VectorStore:
    def __init__(self):
        self.index_path = INDEX_DIR / "faiss.index"
        self.meta_path = INDEX_DIR / "meta.json"
        self.index = faiss.IndexFlatIP(EMBED_DIM)
        self.meta = {}
        self._load()

    def _load(self):
        if self.index_path.exists():
            self.index = faiss.read_index(str(self.index_path))
        if self.meta_path.exists():
            self.meta = json.loads(self.meta_path.read_text(encoding="utf-8"))

    def _save(self):
        faiss.write_index(self.index, str(self.index_path))
        self.meta_path.write_text(
            json.dumps(self.meta, ensure_ascii=False), encoding="utf-8"
        )

    def add(self, vector, text, language, source):
        new_id = str(self.index.ntotal)
        self.index.add(vector)
        self.meta[new_id] = {
            "text": text, "language": language, "source": source
        }
        self._save()
        return new_id

    def search(self, vector, k=3):
        if self.index.ntotal == 0:
            return []
        scores, ids = self.index.search(vector, k)
        out = []
        for s, i in zip(scores[0], ids[0]):
            if i == -1:
                continue
            m = self.meta.get(str(i), {})
            out.append({
                "id": str(i),
                "text": m.get("text", ""),
                "score": round(float(s), 4),
                "language": m.get("language", "unknown"),
                "source": m.get("source", ""),
            })
        return out


_store = None


def get_store():
    global _store
    if _store is None:
        _store = VectorStore()
    return _store
```

**Why JSON sidecar?** FAISS only stores vectors. It can't store text or metadata. So we save a JSON dict alongside the index mapping each ID to its text, language, and source.

**Your choices:**
- Rename class to `DocStore` or `FaissStore`
- Rename `add`/`search` to `insert`/`query`
- Rename `out` to `results` or `hits`
- Rename `meta` to `metadata` or `docs`
- Change score rounding to `round(float(s), 3)`
- Rename `_store`/`get_store` to `_instance`/`get_instance`

---

## Step 6: Language Detection + Translation (app/services/lang.py)

```python
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0


def detect_language(text):
    code = detect(text)
    if code.startswith("ja"):
        return "ja"
    return "en"


_models = {}


def _get_model(src, tgt):
    key = (src, tgt)
    if key not in _models:
        from transformers import MarianMTModel, MarianTokenizer
        name = f"Helsinki-NLP/opus-mt-{src}-{tgt}"
        if src == "en" and tgt == "ja":
            name = "Helsinki-NLP/opus-mt-en-jap"
        tokenizer = MarianTokenizer.from_pretrained(name)
        model = MarianMTModel.from_pretrained(name)
        _models[key] = (tokenizer, model)
    return _models[key]


def translate(text, src, tgt):
    if src == tgt:
        return text
    tokenizer, model = _get_model(src, tgt)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_length=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
```

**Why MarianMT?** Works offline, no API key needed, open-source. `googletrans` is an unofficial wrapper that breaks often.

**Why `en-jap` not `en-ja`?** Helsinki-NLP named their English-to-Japanese model `opus-mt-en-jap`, not `opus-mt-en-ja`. The Japanese-to-English model is `opus-mt-ja-en` though. Inconsistent naming on their side.

**Why `DetectorFactory.seed = 0`?** `langdetect` uses random sampling internally. Setting a seed makes detection deterministic so tests don't flake.

**Your choices:**
- Rename `detect_language` to `detect_lang` or `get_lang`
- Rename `translate` to `translate_text` or `convert`
- Rename `_models` to `_cache` or `_translators`
- Rename `_get_model` to `_load_translator` or `_init_model`

---

## Step 7: Mock LLM (app/services/rag.py)

```python
def build_prompt(query, docs):
    context = "\n---\n".join(d["text"] for d in docs)
    return f"Question: {query}\n\nContext:\n{context}"


def mock_llm_answer(query, docs):
    if not docs:
        return f"No documents found for: {query}"
    sources = ", ".join(d["source"] for d in docs)
    snippets = " ".join(d["text"][:200] for d in docs[:2])
    return (
        f"Based on {len(docs)} retrieved document(s) ({sources}), "
        f"the most relevant information is: {snippets}"
    )
```

**Your choices:**
- Rename `build_prompt` to `format_prompt` or `make_prompt`
- Rename `mock_llm_answer` to `generate_answer` or `fake_answer`
- Change snippet length from `200` to `150` or `100`
- Change `docs[:2]` to `docs[:3]` (use more docs in answer)
- Change the response format entirely — it's a mock, anything works

---

## Step 8: Ingest Router (app/routers/ingest.py)

```python
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.auth import verify_key
from app.services import embedder, store
from app.services.lang import detect_language
from app.models import IngestResponse

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse,
             dependencies=[Depends(verify_key)])
async def ingest(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(400, "Only .txt files accepted")
    raw = await file.read()
    text = raw.decode("utf-8").strip()
    if not text:
        raise HTTPException(400, "Empty file")

    lang = detect_language(text)
    vec = embedder.encode(text)
    s = store.get_store()
    new_id = s.add(vec, text=text, language=lang, source=file.filename)

    return IngestResponse(
        id=new_id, language=lang, num_chunks=1, source=file.filename
    )
```

**Your choices:**
- Rename `raw`/`text` to `content`/`body` or `data`/`doc`
- Rename `lang` to `detected` or `language`
- Rename `vec` to `embedding` or `vector`
- Rename `s` to `vs` or `db` or inline `store.get_store().add(...)`
- Change error messages

---

## Step 9: Retrieve Router (app/routers/retrieve.py)

```python
from fastapi import APIRouter, Depends
from app.auth import verify_key
from app.services import embedder, store
from app.services.lang import detect_language
from app.models import RetrieveRequest, RetrieveResponse

router = APIRouter()


@router.post("/retrieve", response_model=RetrieveResponse,
             dependencies=[Depends(verify_key)])
def retrieve(req: RetrieveRequest):
    vec = embedder.encode(req.query)
    hits = store.get_store().search(vec, k=req.top_k)
    return RetrieveResponse(
        query_language=detect_language(req.query),
        results=hits,
    )
```

**Your choices:**
- Rename `req` to `body` or `payload`
- Rename `vec` to `embedding` or `q_vec`
- Rename `hits` to `results` or `docs` or `matches`

---

## Step 10: Generate Router (app/routers/generate.py)

```python
from fastapi import APIRouter, Depends
from app.auth import verify_key
from app.services import embedder, store, rag
from app.services.lang import detect_language, translate
from app.models import GenerateRequest, GenerateResponse

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse,
             dependencies=[Depends(verify_key)])
def generate(req: GenerateRequest):
    query_lang = detect_language(req.query)
    out_lang = req.output_language or query_lang

    vec = embedder.encode(req.query)
    docs = store.get_store().search(vec, k=3)
    answer = rag.mock_llm_answer(req.query, docs)

    if out_lang != query_lang:
        answer = translate(answer, src=query_lang, tgt=out_lang)

    return GenerateResponse(
        query_language=query_lang,
        output_language=out_lang,
        answer=answer,
        sources=[{"id": d["id"], "source": d["source"], "score": d["score"]}
                 for d in docs],
    )
```

**Your choices:**
- Rename `query_lang`/`out_lang` to `q_lang`/`target` or `src_lang`/`tgt_lang`
- Build sources list with a loop instead of list comprehension
- Rename `docs` to `hits` or `results`

---

## Step 11: Main App (app/main.py)

```python
from fastapi import FastAPI
from app.routers import ingest, retrieve, generate

app = FastAPI(title="Healthcare RAG", version="0.1.0")

app.include_router(ingest.router)
app.include_router(retrieve.router)
app.include_router(generate.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
```

**Your choices:**
- Change the title
- Rename `healthz` to `health_check` or `ping`
- Change endpoint path to `/health` or `/ping`

---

## Step 12: Tests

### tests/conftest.py

```python
import os
import tempfile
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def api_key():
    return "test-key"


@pytest.fixture(scope="session", autouse=True)
def env(api_key):
    os.environ["API_KEY"] = api_key
    os.environ["INDEX_DIR"] = tempfile.mkdtemp()
    yield


@pytest.fixture
def client():
    from app.main import app
    return TestClient(app)
```

Important: env vars must be set BEFORE `app.main` is imported because `settings.py` reads them at import time.

### tests/test_auth.py

```python
def test_missing_api_key(client):
    resp = client.post("/retrieve", json={"query": "test"})
    assert resp.status_code == 401


def test_wrong_api_key(client):
    resp = client.post(
        "/retrieve",
        json={"query": "test"},
        headers={"X-API-Key": "wrong-key"},
    )
    assert resp.status_code == 401
```

### tests/test_ingest.py

```python
import io


def test_ingest_en(client, api_key):
    content = b"Type 2 diabetes management focuses on lifestyle changes."
    resp = client.post(
        "/ingest",
        files={"file": ("diabetes.txt", io.BytesIO(content), "text/plain")},
        headers={"X-API-Key": api_key},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["language"] == "en"
    assert data["source"] == "diabetes.txt"
    assert data["num_chunks"] == 1


def test_ingest_ja(client, api_key):
    content = "2型糖尿病の管理では生活習慣の改善が重要です。".encode("utf-8")
    resp = client.post(
        "/ingest",
        files={"file": ("diabetes_ja.txt", io.BytesIO(content), "text/plain")},
        headers={"X-API-Key": api_key},
    )
    assert resp.status_code == 200
    assert resp.json()["language"] == "ja"


def test_ingest_rejects_non_txt(client, api_key):
    resp = client.post(
        "/ingest",
        files={"file": ("data.csv", io.BytesIO(b"a,b,c"), "text/plain")},
        headers={"X-API-Key": api_key},
    )
    assert resp.status_code == 400
```

### tests/test_retrieve.py

```python
import io


def _ingest(client, api_key, filename, text):
    client.post(
        "/ingest",
        files={"file": (filename, io.BytesIO(text.encode("utf-8")), "text/plain")},
        headers={"X-API-Key": api_key},
    )


def test_retrieve_returns_results(client, api_key):
    _ingest(client, api_key, "bp.txt",
            "Blood pressure management and hypertension treatment guidelines.")
    _ingest(client, api_key, "asthma.txt",
            "Asthma treatment with inhaled corticosteroids.")
    _ingest(client, api_key, "diabetes2.txt",
            "Diabetes care and insulin therapy.")

    resp = client.post(
        "/retrieve",
        json={"query": "How to manage blood pressure?"},
        headers={"X-API-Key": api_key},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["results"]) >= 1
    assert data["query_language"] == "en"


def test_retrieve_empty_query_rejected(client, api_key):
    resp = client.post(
        "/retrieve",
        json={"query": ""},
        headers={"X-API-Key": api_key},
    )
    assert resp.status_code == 422
```

### tests/test_generate.py

```python
import io


def test_generate_returns_answer(client, api_key):
    client.post(
        "/ingest",
        files={"file": ("gen_test.txt",
               io.BytesIO(b"Metformin is first-line for type 2 diabetes."),
               "text/plain")},
        headers={"X-API-Key": api_key},
    )
    resp = client.post(
        "/generate",
        json={"query": "What is the first line treatment for diabetes?"},
        headers={"X-API-Key": api_key},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "answer" in data
    assert len(data["sources"]) >= 1
    assert data["query_language"] == "en"


def test_health(client):
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
```

**Your choices:**
- Change test function names: `test_ingest_english`, `test_upload_en`
- Change medical text content to different sentences
- Change helper function name `_ingest` to `_upload` or `_add_doc`
- Add more tests if you want

---

## Step 13: Sample Documents (docs/)

Create 5 .txt files. Write your own medical content or use these as reference:

**docs/diabetes_en.txt**
```
Type 2 diabetes management focuses on lifestyle modification including diet,
regular physical activity, and weight management. First-line pharmacological
therapy is metformin. HbA1c should be measured every three to six months.
Patients with cardiovascular risk may benefit from SGLT2 inhibitors or GLP-1
receptor agonists.
```

**docs/hypertension_en.txt**
```
Adults with stage 1 hypertension and a 10-year cardiovascular risk above
ten percent should begin antihypertensive therapy. Target blood pressure
is below 130/80 mmHg. Lifestyle changes include the DASH diet, sodium
restriction, regular aerobic exercise, and limiting alcohol intake.
```

**docs/asthma_en.txt**
```
Asthma severity guides controller therapy. Mild persistent asthma is
treated with low-dose inhaled corticosteroids. Moderate asthma adds a
long-acting beta agonist. Severe asthma may require biologics targeting
IgE or interleukin pathways. Inhaler technique should be reviewed at
every visit.
```

**docs/diabetes_ja.txt**
```
2型糖尿病の管理では、食事療法、定期的な運動、体重管理を含む生活習慣の改善が
重要です。第一選択の薬物療法はメトホルミンです。HbA1cは3〜6ヶ月ごとに
測定する必要があります。心血管リスクのある患者には、SGLT2阻害薬または
GLP-1受容体作動薬が有益な場合があります。
```

**docs/cancer_screening_ja.txt**
```
がん検診のガイドラインでは、50歳から74歳までの成人に対して2年ごとの
大腸がん検診を推奨しています。乳がん検診は40歳から開始し、子宮頸がん
検診は21歳から開始することが推奨されています。喫煙者には低線量CTによる
肺がん検診が推奨されます。
```

---

## Step 14: Dockerfile

```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN python -c "from sentence_transformers import SentenceTransformer; \
    SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')"

COPY app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Step 15: CI/CD (.github/workflows/ci.yml)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip
      - run: pip install -r requirements.txt
      - run: ruff check app
      - run: pytest -q

  docker:
    needs: lint-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

---

## Step 16: README.md

Write your own README. Include these sections:

1. **Title + one-liner** — what this project does
2. **Setup** — venv, install, run commands
3. **Environment Variables** — API_KEY, MODEL_NAME, INDEX_DIR
4. **API** — curl examples for /ingest, /retrieve, /generate
5. **Docker** — build and run commands
6. **Tests** — how to run
7. **Design Notes** — 1-2 paragraphs covering:
   - Why multilingual embeddings (one model handles en+ja, no language routing)
   - FAISS `IndexFlatIP` with normalized vectors gives cosine similarity
   - Scalability: swap to IVF index or managed vector DB for large datasets
   - Mock LLM can be replaced with a real one
   - Chunking strategy needed for longer documents
   - Services are independent modules, easy to swap components

---

## Key Decisions to Understand

| Decision | Why |
|---|---|
| `IndexFlatIP` + normalized vectors | Dot product of unit vectors = cosine similarity |
| JSON sidecar for metadata | FAISS only stores vectors, not text |
| `paraphrase-multilingual-MiniLM-L12-v2` | Handles both EN and JA in one model, 384 dims is lightweight |
| `langdetect` for detection | Simple, no model download needed |
| MarianMT for translation | Works offline, no API key needed, open-source |
| Singleton pattern for model/store | Load once, reuse — avoids reloading on every request |
| `secrets.compare_digest` | Prevents timing attacks on API key comparison |
| `scope="session"` in test fixtures | Env vars + temp dir shared across all tests for speed |

---

## Verification Checklist

After building, verify:
- [ ] `ruff check .` passes
- [ ] `pytest` — all tests pass
- [ ] `uvicorn app.main:app --reload` starts without error
- [ ] `GET /healthz` returns 200
- [ ] `POST /ingest` with .txt returns 200 with language detected
- [ ] `POST /ingest` with .csv returns 400
- [ ] `POST /retrieve` returns ranked results with scores
- [ ] `POST /retrieve` with empty query returns 422
- [ ] Requests without X-API-Key return 401
- [ ] `POST /generate` returns mock answer with sources
- [ ] `POST /generate` with `output_language` triggers translation
- [ ] `docker build` succeeds
