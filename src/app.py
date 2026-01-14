from fastapi import FastAPI, UploadFile, File
from src.utils import model
from src.config.chromadb_config import collection
import uuid
import os

USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "0").lower() == "1"
# Initialize FastAPI app
app = FastAPI()


@app.post("/query")
def query(question: str) -> dict:
    """Endpoint to query the knowledge base and get an answer."""
    
    # Query the ChromaDB collection for relevant documents
    results = collection.query(query_texts=[question], n_results=1)

    # Extract the first document from the results
    context = results['documents'][0][0] if results['documents'][0] else "No relevant document found."

    if USE_MOCK_LLM:
        print("Using mock LLM for response.")
        # Return a mock answer for testing purposes
        return { "answer": f"Mock answer for question: {question} with context: {context}" }
    
    # Generate answer using the model utility
    answer = model.generate_answer(context=context, question=question)

    # Return the answer as a JSON response
    return { "answer": answer }

@app.post("/add")
async def add_knowledge(
    file: UploadFile = File(...),
)-> dict:
    """Endpoint to add knowledge document to ChromaDB collection."""
    try:
        # Read the uploaded file content
        document = (await file.read()).decode("utf-8")

        # Prepare metadata and unique ID for the document
        source = file.filename
        doc_id = str(uuid.uuid4())

        # Add the provided document to the ChromaDB collection
        collection.add(
            documents=[document],
            metadatas=[{"source": source}],
            ids=[doc_id]
        )
        return { 
            "message": "Document added successfully.",
            "id": doc_id,
            "source": source,
            "status": "success"
        }
    except Exception as e:
        return { 
            "message": f"Failed to add document: {str(e)}",
            "status": "error"
        }