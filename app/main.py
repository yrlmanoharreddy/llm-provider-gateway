from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description= "LLM usage sing Direct SDK, LangChain, LlamaIndex, Ollama apis"
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status" : "UP",
        "service": settings.app_name,
        "environment":settings.app_env
    }