const BACKEND_URL = "http://localhost:8000"

const pdfInput = document.getElementById("pdfInput")
const uploadBtn = document.getElementById("uploadBtn")
const uploadStatus = document.getElementById("uploadStatus")
const pdfList = document.getElementById("pdfList")
const chatWindow = document.getElementById("chatWindow")
const questionInput = document.getElementById("questionInput")
const sendBtn = document.getElementById("sendBtn")

uploadBtn.addEventListener("click",async ()=>{
    file=pdfInput.files[0]

    if(!file){
        uploadStatus.textContent='Upload PDF first !!'
    }
    uploadBtn.disabled=true
    uploadBtn.textContent='Uploading...'
    uploadStatus.textContent='Processing PDF...'

    try{
    const formdata=new FormData();
    formdata.append("file",file);
    
    const response = await fetch(`${BACKEND_URL}/upload`,{
        method:"POST",
        body:formdata
    });

    const data = await response.json();
    uploadStatus.textContent=`${data.message}`;

    const item = document.createElement("div");
    item.textContent=`${file.name} (${data.chunks} chunks)`;
    pdfList.appendChild(item);
    }
    catch(error){
        uploadStatus.textContent="Upload Failed";
    }finally{
        uploadBtn.textContent="Upload PDF";
        uploadBtn.disabled=false;
    }
})