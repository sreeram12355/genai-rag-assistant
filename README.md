# GenAI Chat Assistant with RAG

## Project Overview
This project implements a GenAI-powered chat assistant using Retrieval-Augmented Generation (RAG).

The assistant answers user questions by retrieving relevant documents from a knowledge base and generating responses using a Large Language Model.

---

## Tech Stack

Backend:
- Python
- Flask

Frontend:
- HTML
- JavaScript
- CSS

AI Technologies:
- Gemini API (LLM)
- Embeddings
- Cosine similarity search

---

## Project Architecture

User → Chat Interface → Flask API → Embedding Generation → Vector Search → Retrieved Context → Gemini LLM → Response

---

## RAG Workflow

1. User enters a question in the chat interface.
2. The question is converted into an embedding.
3. The system compares the query embedding with document embeddings.
4. The most relevant document chunks are retrieved.
5. The retrieved context is sent to the LLM.
6. The LLM generates a grounded response.

---

## Folder Structure

genai-rag-assistant

app.py  
docs.json  
rag.py  
vector_store.py  
requirements.txt  

templates  
  index.html  

static  
  script.js  
  styles.css  

---

## How to Run the Project

Step 1 – Install dependencies

pip install flask numpy scikit-learn google-genai

Step 2 – Set Gemini API key

set GEMINI_API_KEY=your_api_key_here

Step 3 – Run the server

python app.py

Step 4 – Open browser

http://localhost:5000

---

## Example Questions

- How can I reset my password?
- How do I create an account?
- How do I contact support?

---

## Features

- Document knowledge base
- Embedding generation
- Vector similarity search
- Retrieval-Augmented Generation
- Chat interface
- Context-based responses

---

## Future Improvements

- Use a vector database (FAISS or Pinecone)
- Add better UI
- Add user authentication
- Store chat history in database
