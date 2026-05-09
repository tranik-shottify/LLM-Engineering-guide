import json
import faiss
from app.config import INDEX_DIR, EMBED_DIM


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
