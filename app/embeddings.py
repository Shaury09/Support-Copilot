from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def generate_embedding(text, is_query=False):

    if is_query:
        text = (
            "Represent this sentence for searching relevant passages: "
            + text
        )

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()