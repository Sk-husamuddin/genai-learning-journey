import fitz
import os

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        next_start = end - overlap
        
        # Safety check — always move forward
        if next_start <= start:
            break
            
        start = next_start
    return chunks

def load_pdf(file_path,display_name=None):
    chunks = []
    metadata = []
    
    doc = fitz.open(file_path)
    filename = display_name or os.path.basename(file_path)
    
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        
        # Skip empty pages
        if not text.strip():
            continue
        
        page_chunks = chunk_text(text)
        
        for chunk in page_chunks:
            # Skip empty chunks
            if chunk.strip():
                chunks.append(chunk)
                metadata.append({
                    "source": filename,
                    "page": page_num
                })
    
    print(f"✅ Extracted {len(chunks)} chunks from {filename}")
    return chunks, metadata