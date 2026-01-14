import chromadb
from src.config.settings import Settings
from chromadb.utils import embedding_functions

embedding_functions.ONNXMiniLM_L6_V2.DOWNLOAD_PATH=Settings.CACHE_DIR

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path=Settings.PERSISTENT_DB_PATH)

# Get or create the collection
collection = chroma_client.get_or_create_collection(name=Settings.COLLECTION_NAME)