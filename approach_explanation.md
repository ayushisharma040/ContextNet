# Adobe Hackathon – Round 1B

🧠 Core Idea
We use MiniLM embeddings + graph structure to score the most relevant sections and sub-sections for a persona and job objective.

📌 Round 1A
- Parse PDFs and extract heading text
- Embed headings using MiniLM
- Build similarity graph via cosine + thresholding

📌 Round 1B
- Accept persona + job string
- Generate query vector
- Rank sections by semantic + graph centrality score
- Extract refined paragraphs for sub-section relevance

🎯 Scoring Optimization

| Metric             | Approach                          |
|--------------------|-----------------------------------|
| Section Relevance  | Centrality-weighted similarity    |
| Subsection Relevance | Top 3 semantically close paragraphs |

📦 Output Format
See `app/output/top_sections.json`