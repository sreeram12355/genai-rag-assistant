import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

documents = []
embeddings = []


def load_documents():
    global documents

    with open("docs.json", "r") as f:
        documents = json.load(f)


def generate_embedding(text):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def build_vector_store():
    global embeddings

    for doc in documents:
        emb = generate_embedding(doc["content"])
        embeddings.append(emb)


def search(query_embedding, top_k=3):

    similarities = cosine_similarity([query_embedding], embeddings)[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for idx in top_indices:
        results.append((documents[idx], similarities[idx]))

    return results