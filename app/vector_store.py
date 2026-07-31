import os
import chromadb

print("Current Working Directory:", os.getcwd())

from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "vector_db"

client = chromadb.PersistentClient(path=str(DB_PATH))

collection = client.get_or_create_collection(
    name="support_docs"
)

def store_chunks(chunks, embeddings, metadatas):

    print("Before upsert:", collection.count())

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print("After upsert:", collection.count())


def get_collection():
    return collection