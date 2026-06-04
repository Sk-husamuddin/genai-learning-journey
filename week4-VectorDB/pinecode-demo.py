import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

load_dotenv()

api_key=os.getenv("PINECONE_API_KEY")
pc=Pinecone(api_key=api_key)

index_name = "my-first-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name = index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws",region="us-east-1")
    )

index = pc.index(index_name)

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Cars are fast vehicles used for transportation",
    "Dogs are loyal animals and great pets",
    "Automobiles revolutionized modern travel",
    "Cats are independent and curious animals",
    "Electric vehicles are the future of transport",
]

vectors = []

for i,doc in enumerate(documents):
    embeddings = model.encode(doc).tolist()
    vectors.append(
        (f"doc{i+1}",embeddings,{"text":doc})
    )
index.upsert(vectors=vectors)

query = "I need a furry pet"
query_embeds = model.encode(query).tolist()
results=index.query(vector=query_embeds,top_k=3,include_metadata=True)

print("Top results \n")
for match in results["matches"]:
    print(f"  Score: {match.score:.4f} → {match.metadata['text']}")