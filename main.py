from fastapi import FastAPI
from api.routes import router

app=FastAPI(title="Jordan360 AI Backend")

app.include_router(router)

@app.get("/health")
def health():
    return {"status":"running"}
