from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def getmsg():
    return {
        "message":"Backend is live"
    }