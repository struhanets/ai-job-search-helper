from fastapi import FastAPI
from app.api.routers.health import router as health_router
from app.api.routers.ai import router as ai_router

app = FastAPI()

app.include_router(health_router)
app.include_router(ai_router)