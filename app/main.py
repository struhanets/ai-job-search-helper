from fastapi import FastAPI
from app.api.routers.health import router as health_router
from app.api.routers.ai import router as ai_router
from app.api.routers.cv import router as cv_router

app = FastAPI()

app.include_router(health_router)
app.include_router(ai_router)
app.include_router(cv_router)
