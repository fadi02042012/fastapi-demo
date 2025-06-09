from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "أهلاً بك في API!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"مرحبًا يا {name}!"}
