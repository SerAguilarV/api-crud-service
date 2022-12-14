from fastapi import FastAPI

from app.controller import controller

app = FastAPI(debug=True, docs_url="/docs", openapi_url="/openapi.json", redoc_url="/redoc")
app.include_router(controller.router)
