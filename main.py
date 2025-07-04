from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "TODO: 여기에 응답 문자열을 작성하세요."
