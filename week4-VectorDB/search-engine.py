import chromadb
from documents import Documents

client = chromadb.Client()

collections = client.get_or_create_collection(name="knowledge_base")

collections.add(
    documents=Documents,
    ids=[f"{i+1}" for i in range(len(Documents))]
)

print("Search Engine Ready !!")
print("="*40)

while True:
    query = input("\nEnter search query (or 'quit' to exit):\n> ")
    if query.lower()=="quit":
        print("Goodbye")
        break

    result = collections.query(
        query_texts=query,
        n_results=2,
        include=["documents","distances"]
    )

    documents = result["documents"][0]
    distances = result["distances"][0]

    found = False
    for doc,dist in zip(documents,distances):
        similarity = 1-dist
        if similarity >0:
            print(f"score:{similarity:.2f}:->{doc}")
            found = True
    if not found:
        print("No results found")