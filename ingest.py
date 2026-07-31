from pathlib import Path

from app.loaders import load_markdown
from app.chunker import create_chunks
from app.embeddings import generate_embedding
from app.vector_store import store_chunks
from app.bm25_index import build_bm25, save_bm25

all_chunks = []
all_embeddings = []
all_metadatas = []

for file in Path("docs").glob("*.md"):

    print(f"Indexing {file.name}")

    doc = load_markdown(file)

    chunks = create_chunks(doc["text"])

    for chunk in chunks:
        all_chunks.append(chunk)
        all_embeddings.append(generate_embedding(chunk))
        all_metadatas.append(doc["metadata"])

store_chunks(
    all_chunks,
    all_embeddings,
    all_metadatas
)

build_bm25(
    all_chunks,
    all_metadatas
)
save_bm25()

print(f"\n✅ Indexed {len(all_chunks)} chunks.")