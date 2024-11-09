import os
import dotenv
from pathlib import Path

dotenv.load_dotenv()

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

def get_query_index():
    PERSIST_DIR = "./storage"
    
    try:
        if not os.path.exists(PERSIST_DIR):
            # Ensure data directory exists
            if not os.path.exists("data"):
                raise FileNotFoundError("Data directory not found")
                
            # load the documents and create the index
            documents = SimpleDirectoryReader("data").load_data()
            index = VectorStoreIndex.from_documents(documents)
            # store it for later
            Path(PERSIST_DIR).mkdir(exist_ok=True)
            index.storage_context.persist(persist_dir=PERSIST_DIR)
        else:
            # load the existing index
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)

        # Either way we can now query the index
        return index.as_query_engine()
        
    except Exception as e:
        print(f"Error initializing query index: {str(e)}")
        return None

def answer_query(query):
    if not query or len(query) == 0:
        return None

    query_engine = get_query_index()
    if query_engine is None:
        return None
        
    try:
        response = query_engine.query(query)
        return response
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        return None