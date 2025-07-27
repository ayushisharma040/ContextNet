def graph_to_json(G):
    result = []
    for node, data in G.nodes(data=True):
        connections = [G.nodes[n]['text'] for n in G.neighbors(node)]
        result.append({
            "level": data["level"],
            "text": data["text"],
            "page": data["page"],
            "connected_to": connections
        })
    return result