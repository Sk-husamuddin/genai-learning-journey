import os
from pdf_loader import load_pdf
from vector_store import add_pdf_to_collection
from rag_engine import get_answer


def load_pdfs():
    while True:
        path = input("\nEnter the pdf path or 'done' to start chatting:")
        if path.lower()=='done':
            break

        if not os.path.exists(path):
            print("File not found. Try again")
            continue
        
        if not path.endswith(".pdf"):
            print("Only PDF files are accepted")
            continue

        print(f"{path} loading...")
        chunks,metadata=load_pdf(path)
        file_name=os.path.basename(path)
        add_pdf_to_collection(chunks,metadata,file_name)
        print(f"{file_name} loaded successfully")

def chat_loop():
    print("Chatbot Ready !!")
    print("="*40)
    print("\nAsk questions from the PDF's")
    print("\nType 'quit' to exit\n")

    while True:
        question=input("You:")
        if question.lower()=='quit':
            print("Goodbye !!")
            break

        if not question.strip():
            print("Enter the question !!")
            continue

        print("Thinking...")

        answer,sources=get_answer(question)
        print(f"\nAnswer: {answer}")

        print("\nSources:")

        for source in sources:
            print(f" {source}")

        print("="*40)

if __name__=="__main__":
    load_pdfs()
    chat_loop()