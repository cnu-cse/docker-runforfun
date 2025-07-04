from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "hello cnu computer network is fun"
