from app.vector_store import get_collection

collection = get_collection()

print("Count:", collection.count())