from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="AI Career Copilot"
)

app.include_router(
    api_router,
    prefix="/api/v1"
)

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
