import os
import uuid
from src.config.chromadb_config import collection

# Build the file path relative to the working directory
folder_path = os.path.join(os.getcwd(), 'src', 'data')

# Read text data from a file
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            text = file.read()

            # Add the text data to the collection with metadata and a unique ID
            collection.add(
                documents=[text],
                metadatas=[{"source": filename}],
                ids=[f"{str(uuid.uuid4())}"]
            )
        


print("Document added to the 'docs' collection in ChromaDB.")
