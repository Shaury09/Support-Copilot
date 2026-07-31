from app.vector_store import get_collection

collection = get_collection()

data = collection.get()

print("Number of chunks:", len(data["documents"]))

for i, doc in enumerate(data["documents"]):
    print("=" * 60)
    print("ID:", data["ids"][i])
    print(doc)