from sentence_transformers import SentenceTransformer
import faiss

class RAG:
    def __init__(self, documents):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.sentences = documents.split(". ")
        self.embeddings = self.model.encode(self.sentences)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def retrieve_passages(self, query, k=5):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(query_embedding, k)
        return [self.sentences[i] for i in I[0]]
