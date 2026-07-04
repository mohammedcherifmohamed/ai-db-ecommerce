import ollama 

from app.interface.embedding_provider import EmbeddingProvider

class OllamaEmbeddingProvider(EmbeddingProvider):

    def __init__(self,model:str):
        self.model = model

    def embed(self,texts:list[str]) -> list[list[str]]:

        response = ollama.embed(
            model=self.model,
            input=texts
        )

        return response["embeddings"]
    