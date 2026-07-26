from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel

import models
import schemas
import crud
import assistant

from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scholarship Tracker API")

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5501",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Model for Assistant
# -----------------------------
class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Scholarship Tracker API is running"}


# -----------------------------
# Student APIs
# -----------------------------

@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)


@app.get("/students", response_model=list[schemas.Student])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# -----------------------------
# Scholarship APIs
# -----------------------------

@app.post("/scholarships", response_model=schemas.Scholarship)
def create_scholarship(
    scholarship: schemas.ScholarshipCreate,
    db: Session = Depends(get_db)
):
    return crud.create_scholarship(db, scholarship)


@app.get("/scholarships", response_model=list[schemas.Scholarship])
def get_scholarships(db: Session = Depends(get_db)):
    return crud.get_scholarships(db)


# -----------------------------
# Application APIs
# -----------------------------

@app.post("/applications", response_model=schemas.Application)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db)
):
    return crud.create_application(db, application)


@app.get("/applications", response_model=list[schemas.Application])
def get_applications(db: Session = Depends(get_db)):
    return crud.get_applications(db)


@app.get("/applications/{application_id}", response_model=schemas.Application)
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = crud.get_application(db, application_id)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    return application


@app.put("/applications/{application_id}")
def update_application(
    application_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    application = crud.update_application_status(db, application_id, status)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    return application


@app.delete("/applications/{application_id}")
def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = crud.delete_application(db, application_id)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    return {"message": "Application deleted successfully"}


# -----------------------------
# AI Assistant API
# -----------------------------

@app.post("/assistant")
def ask_question(data: Question, db: Session = Depends(get_db)):
    answer = assistant.get_response(data.question, db)
    return {
        "question": data.question,
        "answer": answer
    }