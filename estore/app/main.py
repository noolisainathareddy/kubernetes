from symbol import return_stmt

from fastapi import FastAPI

app  = FastAPI()

@app.get("/health")
def health():
    return "EStore is up and running"


@app.get("/ides")
def idea():
    return "Testing ESTORE with this setup"
