from fastapi import APIRouter, Depends
from app.deps import verify_api_key
from app.services import embeddings, vector_store
from app.services.language import detect_language
from app.schemas import RetrieveRequest, RetrieveResponse

router = APIRouter()


@router.post("/retrieve", response_model=RetrieveResponse,
             dependencies=[Depends(verify_api_key)])
def retrieve(req: RetrieveRequest):
    vec = embeddings.encode(req.query)
    hits = vector_store.get_store().search(vec, k=req.top_k)
    return RetrieveResponse(
        query_language=detect_language(req.query),
        results=hits,
    )
