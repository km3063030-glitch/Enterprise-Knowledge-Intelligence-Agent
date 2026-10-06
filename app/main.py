from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Enterprise RAG Knowledge Agent",
    description="AI-powered enterprise document assistant",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return{
        "message": "Enterprise RAG Knowledge Agent running"
    }

@app.get("/health")
def health_check():
    return{
        "status": "healthy"
    }
