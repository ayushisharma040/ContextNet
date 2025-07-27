from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_sections(G, query_vec):
    ranked = []
    for node, data in G.nodes(data=True):
        sec_vec = model.encode(data["text"])
        sim = cosine_similarity([query_vec], [sec_vec])[0][0]
        centrality = nx.pagerank(G)[node]
        score = 0.7 * sim + 0.3 * centrality
        ranked.append((score, data))
    ranked.sort(reverse=True)
    return ranked[:5]