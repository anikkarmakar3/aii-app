import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

@app.get("/config")
def config():
    return {
        "db_host": DB_HOST,
        "db_port": DB_PORT
    }

@app.get("/")
def home():
    return {"message": "API Working"}

@app.get("/health")
def health():
    return {"status": "healthy"}