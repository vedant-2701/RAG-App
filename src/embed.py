import os
from src.config.chromadb_config import collection

# Build the file path relative to the working directory
file_path = os.path.join(os.getcwd(), 'src', 'data', 'k8s.txt')

# Read text data from a file
with open(file_path, "r") as f:
    text = f.read()

# Add the text data to the collection with metadata and a unique ID
collection.add(
    documents=[text],
    metadatas=[{"source": "k8s.txt"}],
    ids=["k8s_doc_1"]
)

print("Document added to the 'docs' collection in ChromaDB.")
