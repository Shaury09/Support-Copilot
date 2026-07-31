from collections import defaultdict

from app.retriever import dense_search
from app.bm25_index import search_bm25, load_bm25

load_bm25()


def reciprocal_rank_fusion(dense_results, bm25_results, k=60):

    scores = defaultdict(float)
    chunk_info = {}

    # Dense Retrieval
    for rank, result in enumerate(dense_results, start=1):

        chunk_id = result["id"]

        scores[chunk_id] += 1 / (k + rank)

        chunk_info[chunk_id] = {
            "document": result["document"],
            "metadata": result["metadata"]
        }

    # BM25 Retrieval
    for rank, result in enumerate(bm25_results, start=1):

        chunk_id = result["id"]

        scores[chunk_id] += 1 / (k + rank)

        # If the chunk already exists from dense retrieval,
        # keep the existing info. Otherwise, add it.
        if chunk_id not in chunk_info:
            chunk_info[chunk_id] = {
                "document": result["document"],
                "metadata": result["metadata"]
            }

    fused = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    output = []

    for chunk_id, score in fused:

        output.append({
            "id": chunk_id,
            "document": chunk_info[chunk_id]["document"],
            "metadata": chunk_info[chunk_id]["metadata"],
            "rrf_score": score
        })

    return output


def hybrid_search(query, top_k=5):

    dense_results = dense_search(query, top_k=top_k)
    bm25_results = search_bm25(query, top_k=top_k)

    fused_results = reciprocal_rank_fusion(
        dense_results,
        bm25_results
    )

    return fused_results