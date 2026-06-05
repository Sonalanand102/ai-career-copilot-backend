from fastapi import FastAPI

app = FastAPI(
    title="AI Career Copilot"
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }