from app.interfaces.embedding_provider import EmbeddingProvider

class EmbeddingService:
    def __init__(self,provider:EmbeddingProvider):
        self.provider = provider

    def generate(self,texts:list[str]) -> list[list[float]]:

        if not texts:
            return [] 
        
        return self.provider.embed(texts)
    
    