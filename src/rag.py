from pathlib import Path
import math

from ollama import embed


KNOWLEDGE_BASE = Path(__file__).parent.parent / "knowledge_base"

EMBEDDING_MODEL = "nomic-embed-text"

documents = []


def cosine_similarity(vector_a, vector_b):
    """Calculate cosine similarity between two vectors."""

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def create_embedding(text):
    """Convert text into an embedding."""

    response = embed(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return response.embeddings[0]


def load_knowledge_base():
    """Load all non-empty text files."""

    global documents

    documents = []

    for file_path in KNOWLEDGE_BASE.glob("*.txt"):
        text = file_path.read_text(
            encoding="utf-8"
        ).strip()

        if not text:
            continue

        embedding = create_embedding(text)

        documents.append(
            {
                "source": file_path.name,
                "text": text,
                "embedding": embedding,
            }
        )

    print(
        f"Loaded {len(documents)} knowledge-base documents."
    )


def search_knowledge_base(query, top_k=2):
    """Find the most relevant documents."""

    if not documents:
        load_knowledge_base()

    query_embedding = create_embedding(query)

    results = []

    for document in documents:
        score = cosine_similarity(
            query_embedding,
            document["embedding"],
        )

        results.append(
            {
                "source": document["source"],
                "text": document["text"],
                "score": score,
            }
        )

    results.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return results[:top_k]


if __name__ == "__main__":

    load_knowledge_base()

    query = "My Wi-Fi is connected but I have no internet."

    results = search_knowledge_base(query)

    print("\nUser question:")
    print(query)

    print("\nRAG results:\n")

    for result in results:
        print(f"Source: {result['source']}")

        print(
            f"Similarity: {result['score']:.4f}"
        )

        print(
            f"Content:\n{result['text'][:300]}..."
        )

        print("-" * 60)
