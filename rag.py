import os
import google.generativeai as genai
from vector_store import generate_embedding, search

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

SIMILARITY_THRESHOLD = 0.5


def generate_answer(question, history):

    query_embedding = generate_embedding(question)

    results = search(query_embedding)

    context_chunks = []

    for doc, score in results:
        if score > SIMILARITY_THRESHOLD:
            context_chunks.append(doc["content"])

    if len(context_chunks) == 0:
        return "Sorry, I don't have enough information to answer that.", 0, []

    context = "\n".join(context_chunks)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    answer = response.text

    return answer, 0, context_chunks