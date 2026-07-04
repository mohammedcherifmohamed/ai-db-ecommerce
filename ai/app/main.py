from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.products import router as document_router


app = FastAPI(
    title = "AI Ecommerce",
    version = "1.0.0",
    )

app.includerouter(health_router)
app.includerouter(document_router)