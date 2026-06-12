import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-miniLM-L6-v2')

client = chromadb.PersistentClient("./chroma_db")

collection = client.get_or_create_collection(
    name="pdf_collection",
    metadata={"hnsw:space":"cosine"}
)

def add_pdf_to_collection(chunks,metadata,pdfname):
    #create uniuque ids for each chunks
    existing=collection.count()
    ids=[f"{pdfname}_chunk{existing+i+1}"
         for i in range(len(chunks))
         ]
    
    embeddings=model.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata,
        ids=ids
    )
    print(f"added {len(chunks)} chunks from {pdfname}")

def search(query,n_results=3):
    query_embeddings=model.encode(query).tolist()

    results=collection.query(
        query_embeddings=[query_embeddings],
        n_results=n_results,
        include=["metadatas","documents","distances"]
    )

    chunks=results["documents"][0]
    metadatas=results["metadatas"][0]

    return chunks,metadatas