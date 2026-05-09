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
