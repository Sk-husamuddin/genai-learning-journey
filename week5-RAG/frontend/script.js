const BACKEND_URL = "http://localhost:8000"

const pdfInput = document.getElementById("pdfInput")
const uploadBtn = document.getElementById("uploadBtn")
const uploadStatus = document.getElementById("uploadStatus")
const pdfList = document.getElementById("pdfList")
const chatWindow = document.getElementById("chatWindow")
const questionInput = document.getElementById("questionInput")
const sendBtn = document.getElementById("sendBtn")

const session_id = crypto.randomUUID();

uploadBtn.addEventListener("click",async ()=>{
    const file=pdfInput.files[0]

    if(!file){
        uploadStatus.textContent='Upload PDF first !!'
        return;
    }
    uploadBtn.disabled=true
    uploadBtn.textContent='Uploading...'
    uploadStatus.textContent='Processing PDF...'

    try{
    const formdata=new FormData();
    formdata.append("file",file);
    formdata.append("session_id",session_id);
    
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
        uploadStatus.textContent=`Upload Failed - ${error}`;
    }finally{
        uploadBtn.textContent="Upload PDF";
        uploadBtn.disabled=false;
    }
})

function addmessage(text,sender,sources=[]){
    const message = document.createElement("div");
    message.classList.add("message");

    if(sender=="user"){
        message.classList.add("user-message");
        message.textContent=`You: ${text}`;
    }
    else{
        message.classList.add("bot-message");
        message.textContent=`Bot: ${text}`;

        if(sources.length>0){
            const sourcediv = document.createElement("div");
            sourcediv.classList.add("sources");
            sourcediv.textContent=`Sources: `;

            sources.forEach(source=>{
                const sourceitem = document.createElement("div");
                sourceitem.textContent=source;
                sourcediv.appendChild(sourceitem);
            });
            message.appendChild(sourcediv);
        }
    }   
    chatWindow.appendChild(message);

    chatWindow.scrollTop=chatWindow.scrollHeight;

}

sendBtn.addEventListener("click",async ()=>{
    const question = questionInput.value.trim()

    if(!question){
        return;
    }

    addmessage(question,"user");
    sendBtn.disabled=true;
    sendBtn.textContent="...";
    questionInput.value="";

    try{
        const response = await fetch(`${BACKEND_URL}/ask`,{
                            method:"POST",
                            headers:{
                                "Content-Type":"application/json"
                            },
                            body:JSON.stringify({
                                question:question,
                                session_id:session_id
                            })
        });

        const data = await response.json();

        addmessage(data.answer,"bot",data.sources);
    }
    catch(error){
        addmessage("Error connecting to Server","bot");
    }finally{
        sendBtn.disabled=false;
        sendBtn.textContent="->"
    }
});

questionInput.addEventListener("keypress",(event)=>{
    if(event.key==="Enter"){
        sendBtn.click();
    }
});
