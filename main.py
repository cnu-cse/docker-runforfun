from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "hello computer network is fun"
