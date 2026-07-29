from fastapi import FastAPI
from app.core.middleware import setup_middleware

app = FastAPI()
setup_middleware(app)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}