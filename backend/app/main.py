from fastapi import FastAPI

from app.api.logs import router as logs_router


app = FastAPI(
    title="AI Security Monitoring API",
    description="AI-powered security monitoring SaaS",
    version="0.1.0"
)


app.include_router(logs_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Security Monitoring API"
    }