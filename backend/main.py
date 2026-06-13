from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.ticket import Ticket

app = FastAPI(title="OpsPilotAI Backend")

Base.metadata.create_all(bind=engine)

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/status")
def status():
    return {"status": "ok", "service": "OpsPilotAI Backend"}
