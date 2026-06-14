import os
import shutil
from fastapi import FastAPI
from fastapi import UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pdf_loader import load_pdf
from vector_store import add_pdf_to_collection
from rag_engine import get_answer

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

loaded_pdfs=[]

@app.post("/upload")

async def upload_pdf(file:UploadFile=File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error":"Uploaded file should be PDF only !"}
    
    temp_path=f"temp_{file.filename}"

    with open(temp_path,"wb") as f:
        shutil.copyfileobj(file.file,f)
    
    chunks,metadata=load_pdf(temp_path,display_name=file.filename)
    add_pdf_to_collection(chunks,metadata,file.filename)

    os.remove(temp_path)

    if file.filename not in loaded_pdfs:
        loaded_pdfs.append(file.filename)
    
    return {
        "message":f"{file.filename} is successfullt loaded",
        "chunks":len(chunks),
        "total_pdfs":len(loaded_pdfs)
    }

class Question(BaseModel):
    question:str

@app.post("/ask")

async def ask_question(body:Question):

    if not loaded_pdfs:
        return{
            "answer":"Upload PDF first !",
            "sources":[]
        }
    
    if not body.question.strip():
        return{
            "answer":"Enter the Question !",
            "sources":[]
        }
    
    answer,sources=get_answer(body.question)

    return {
        "answer":answer,
        "sources":sources
    }

@app.get("/pdfs")
async def get_pdfs():
    return {
        "pdfs":loaded_pdfs
    }