from app.retriever import dense_search

results = dense_search(
    "How do I reset my password?"
)

documents = results["documents"][0]
distances = results["distances"][0]
ids = results["ids"][0]

for i in range(len(documents)):
    print("=" * 60)
    print("Rank:", i + 1)
    print("Chunk:", ids[i])
    print("Distance:", distances[i])
    print()
    print(documents[i])