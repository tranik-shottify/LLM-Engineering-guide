from sentence_transformers import SentenceTransformer
from app.config import MODEL_NAME

_model = None


def get_embedder():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def encode(texts):
    if isinstance(texts, str):
        texts = [texts]
    vecs = get_embedder().encode(texts, normalize_embeddings=True)
    return vecs.astype("float32")
