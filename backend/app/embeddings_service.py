from sentence_transformers import SentenceTransformer, util

_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _model


def semantic_match(text, candidates, top_k=1):

    model = get_model()
    emb_text = model.encode(text, convert_to_tensor=True)
    emb_cands = model.encode(candidates, convert_to_tensor=True)
    scores = util.cos_sim(emb_text, emb_cands)[0]

    best = scores.topk(min(top_k, len(candidates)))
    indices = best.indices.tolist()
    values = best.values.tolist()

    return [(candidates[i], float(values[idx])) for idx, i in enumerate(indices)]
