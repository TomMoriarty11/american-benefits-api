from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="American Benefits API",
    description="Micro API for finding available benefits programs for educated and employed individuals.",
    version="1.0.0"
)

app.include_router(router)
