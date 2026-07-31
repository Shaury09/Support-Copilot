from app.vector_store import get_collection

collection = get_collection()

print("Number of stored chunks:", collection.count())