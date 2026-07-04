from dotenv import load_dotenv

import os

load_dotenv()

HOST = os.getenv("HOST","127.0.0.1")
PORT = os.getenv("PORT","5000")


CHROMA_PATH = os.getenv("CHROMA_PATH")

EMBEDDINGS_MODEL = os.getenv('EMBEDDING_MODEL', 'nomic-embed-text')
