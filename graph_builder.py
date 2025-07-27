from sentence_transformers import SentenceTransformer
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_graph(headings):
    G = nx.Graph()
    texts = [h["text"] for h in headings]
    vectors = model.encode(texts)

    for i, hi in enumerate(headings):
        G.add_node(i, **hi)

    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            sim = cosine_similarity([vectors[i]], [vectors[j]])[0][0]
            if sim > 0.5:
                G.add_edge(i, j, weight=sim)

    return G