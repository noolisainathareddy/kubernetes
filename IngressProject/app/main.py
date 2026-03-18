from  fastapi import  FastAPI

app = FastAPI()


@app.get("/health")
def healthcheck():
    return {"message", "Ingress Project is up and running"}


@app.get("/idea")
def idea():
    return {"Testing ingress with this setup"}