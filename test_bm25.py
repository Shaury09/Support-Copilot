from app.bm25_index import load_bm25, search_bm25

load_bm25()

results = search_bm25("discount")

for doc, score in results:
    print("=" * 50)
    print("Score:", score)
    print(doc)