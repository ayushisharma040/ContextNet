import fitz  # PyMuPDF

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for span in l["spans"]:
                        if span["size"] > 16:
                            headings.append({
                                "level": "H1" if span["size"] > 20 else "H2",
                                "text": span["text"],
                                "page": page_num + 1
                            })
    return headings