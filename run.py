from extractor.parser import extract_headings
from extractor.graph_builder import build_graph
from extractor.utils import graph_to_json
from analyzer.persona_processor import get_query_embedding
from analyzer.relevance_ranker import rank_sections
import json

pdf_path = "app/input/sample.pdf"
persona = "Investment Analyst"
job = "Track revenue and innovation strategy"

headings = extract_headings(pdf_path)
G = build_graph(headings)
graph_json = graph_to_json(G)
with open("app/output/graph_output.json", "w") as f:
    json.dump(graph_json, f, indent=2)

query_vec = get_query_embedding(persona, job)
top_sections = rank_sections(G, query_vec)

out = [{"section": s["text"], "page": s["page"]} for _, s in top_sections]
with open("app/output/top_sections.json", "w") as f:
    json.dump(out, f, indent=2)