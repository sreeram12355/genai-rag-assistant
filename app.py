from flask import Flask, request, jsonify, render_template
import uuid

from vector_store import load_documents, build_vector_store
from rag import generate_answer

app = Flask(__name__)

sessions = {}

# Load documents and build embeddings
load_documents()
build_vector_store()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.json

    if "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    session_id = data.get("sessionId", str(uuid.uuid4()))
    message = data["message"]

    history = sessions.get(session_id, [])

    answer, tokens, chunks = generate_answer(message, history)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})

    # Keep last 3 message pairs
    sessions[session_id] = history[-6:]

    return jsonify({
        "reply": answer,
        "tokensUsed": tokens,
        "retrievedChunks": len(chunks)
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)