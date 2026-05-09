from fastapi import APIRouter, Depends
from app.deps import verify_api_key
from app.services import embeddings, vector_store, rag
from app.services.language import detect_language, translate
from app.schemas import GenerateRequest, GenerateResponse

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse,
             dependencies=[Depends(verify_api_key)])
def generate(req: GenerateRequest):
    query_lang = detect_language(req.query)
    out_lang = req.output_language or query_lang

    vec = embeddings.encode(req.query)
    docs = vector_store.get_store().search(vec, k=3)
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
