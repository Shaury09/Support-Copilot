from app.hybrid_retriever import hybrid_search

results = hybrid_search("password reset")

for r in results:
    print("=" * 60)
    print(r["id"])
    print(r["rrf_score"])
    print(r["document"])