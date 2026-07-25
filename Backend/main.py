from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scholarship Tracker API")


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
def update_application(application_id: int, status: str, db: Session = Depends(get_db)):
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