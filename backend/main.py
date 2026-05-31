from fastapi import FastAPI

app = FastAPI(title="OpsPilotAI Backend")

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/status")
def status():
    return {"status": "ok", "service": "OpsPilotAI Backend"}
