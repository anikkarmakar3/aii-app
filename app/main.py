from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "version 1 API Working"}

@app.get("/health")
def health():
    return {"status": "healthy"}