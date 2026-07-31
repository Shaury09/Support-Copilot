from app.embeddings import generate_embedding
from app.vector_store import get_collection

collection = get_collection()

def dense_search(query, top_k=5):

    query_embedding = generate_embedding(query, is_query=True)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "distances", "metadatas"]
    )

    output = []

    docs = results["documents"][0]
    ids = results["ids"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    for i in range(len(docs)):
       output.append({
            "id": ids[i],
            "document": docs[i],
            "metadata": metadatas[i],
            "score": distances[i]
        })

    return output