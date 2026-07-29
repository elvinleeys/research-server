from fastapi import FastAPI
from app.core.middleware import setup_middleware
from app.api.v1.chat import router as chat_router

app = FastAPI()
setup_middleware(app)

app.include_router(
    chat_router
)