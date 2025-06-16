import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load your fine-tuned embedding model
embedding_model = SentenceTransformer("renshanhf/weighted-triplet-finetuned-model")

# Example documents
documents = [
    {"doc_id": 1, "text": "Employees are entitled to 20 days of paid vacation."},
    {"doc_id": 2, "text": "Health insurance is provided for all full-time employees."},
    {"doc_id": 3, "text": "Remote work is allowed up to 3 days per week."},
    {"doc_id": 4, "text": "Maternity leave policy allows up to 16 weeks leave."}
]

texts = [doc["text"] for doc in documents]
doc_embeddings = embedding_model.encode(texts)

# Create a FAISS index for efficient similarity search
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

# Function to retrieve relevant documents based on a question

def retrieve_relevant_docs(question, k=3):
    question_embedding = embedding_model.encode([question])
    D, I = index.search(np.array(question_embedding), k=k)
    retrieved_docs = [texts[i] for i in I[0]]
    return retrieved_docs
