import chromadb

client = chromadb.Client()

collections = client.get_or_create_collection(name="my_docs")

collections.add(
    documents=[
        "Cars are fast vehicles used for transportation",
        "Dogs are loyal animals and great pets",
        "Automobiles revolutionized modern travel",
        "Cats are independent and curious animals",
        "Electric vehicles are the future of transport",
    ],
    ids=["id1","id2","id3","id4","id5"]
)

results = collections.query(
    query_texts=["How can i travel faster"],
    n_results=3
)

print(results["documents"][0])
