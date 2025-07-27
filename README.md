# ContextNet – A Memory-Augmented PDF Companion

ContextNet transforms static PDFs into intelligent semantic graphs, helping you prioritize content based on personas.

🔍 Features
- Outline extraction using heading detection
- Graph of semantic relationships (Round 1A)
- Persona-based section ranking (Round 1B)
- Extensible JSON output

🚀 How to Run

```bash
docker build -t contextnet .
docker run -v "$(pwd)/app/input:/app/input" -v "$(pwd)/app/output:/app/output" contextnet
```

📁 Folder Structure
- `app/input`: Place PDFs here
- `app/output`: Extracted output JSONs
- `app/extractor`: Round 1A logic
- `app/analyzer`: Round 1B logic
- `run.py`: Docker entry point