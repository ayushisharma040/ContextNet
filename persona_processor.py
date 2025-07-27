from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_query_embedding(persona, job):
    p = model.encode(persona)
    j = model.encode(job)
    return (p + j) / 2