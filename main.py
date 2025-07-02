from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = client.create_collection(name="documents")

documents = [
    "La inteligencia artificial es una rama de la informática que se centra en crear sistemas capaces de realizar tareas que requieren inteligencia humana.",
    "ChromaDB es una base de datos vectorial de código abierto ideal para trabajar con IA.",
    "Los embeddings son representaciones numéricas del significado de un texto.",
    "Hugging Face ofrece modelos preentrenados de procesamiento de lenguaje natural."   
]

embeddings = model.encode(documents).tolist()
ids = [f"doc{i}" for i in range(len(documents))]
collection.add(documents=documents, embeddings=embeddings, ids=ids)

def answer_question(question):
    embedding_question = model.encode([question]).tolist()[0]
    result = collection.query(query_embeddings=[embedding_question], n_results=1)
    return result["documents"][0][0]

question = input("Ask a question about AI or Chroma: ")
answer = answer_question(question)
print("\nRespuesta aproximada encontrada: ")
print(answer)