from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Scholarship Tracker API is running"}