import os
import json
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

from app.hybrid_retriever import hybrid_search
from app.prompts import SYSTEM_PROMPT

load_dotenv(Path(__file__).resolve().parent / ".env")

print("Loading .env from:", Path(__file__).resolve().parent / ".env")
print("GROQ_API_KEY =", os.getenv("GROQ_API_KEY"))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def build_context(results):
    """
    Build numbered context for the LLM.
    """
    context = ""

    for i, result in enumerate(results[:5], start=1):

        source = result["metadata"]["source"]

        context += f"""
Document {i}
Source: {source}

{result['document']}

-----------------------------------------
"""

    return context


def build_prompt(query, context):

    prompt = f"""
Context:

{context}

Question:

{query}

Answer:
"""

    return prompt


def generate_answer(query):

    # Retrieve documents only once
    results = hybrid_search(query)

    # Build context
    context = build_context(results)

    # Build prompt
    prompt = build_prompt(query, context)

    # Call LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=512,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    raw_response = response.choices[0].message.content.strip()

    # -------------------------------
    # Parse JSON returned by the LLM
    # -------------------------------
    try:

        data = json.loads(raw_response)

        answer = data["answer"]
        citation_numbers = data["citations"]

    except Exception:

        # Fallback if model doesn't return valid JSON
        answer = raw_response

        citation_numbers = list(range(1, min(len(results), 5) + 1))

    # ----------------------------------------
    # Convert citation numbers to source files
    # ----------------------------------------
    seen = set()
    sources = []

    for number in citation_numbers:

        if 1 <= number <= min(len(results), 5):

            source = results[number - 1]["metadata"]["source"]

            if source not in seen:
                seen.add(source)
                sources.append(source)

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":

    question = "How do I reset my password?"

    response = generate_answer(question)

    print("=" * 60)
    print("QUESTION")
    print("=" * 60)
    print(question)

    print()

    print("=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(response["answer"])

    print()

    print("=" * 60)
    print("SOURCES")
    print("=" * 60)

    for source in response["sources"]:
        print("•", source)