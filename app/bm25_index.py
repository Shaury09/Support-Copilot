from rank_bm25 import BM25Okapi
import pickle
import re

bm25 = None
documents = None
metadatas = None


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def build_bm25(chunks, metadata_list ):

    global bm25, documents, metadatas

    documents = chunks
    metadatas = metadata_list

    tokenized = [
        tokenize(chunk)
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized)

    return bm25


def save_bm25():

    with open("bm25.pkl", "wb") as f:
        pickle.dump(
            (bm25, documents, metadatas),
            f
        )


def load_bm25():

    global bm25, documents, metadatas

    with open("bm25.pkl", "rb") as f:
        bm25, documents, metadatas = pickle.load(f)


def search_bm25(query, top_k=5):

    scores = bm25.get_scores(tokenize(query))

    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    results = []

    for idx, score in ranked[:top_k]:
        results.append({
        "id": f"chunk_{idx}",
        "document": documents[idx],
        "metadata": metadatas[idx],
        "score": score
        })

    return results