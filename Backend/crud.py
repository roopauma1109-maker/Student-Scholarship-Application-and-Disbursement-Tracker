from sqlalchemy.orm import Session, joinedload
import models
import schemas

# -------------------------------
# Student CRUD
# -------------------------------

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db: Session):
    return db.query(models.Student).all()


# NEW FUNCTION
def get_student_applications(db: Session, student_id: int):
    return (
        db.query(models.Application)
        .options(
            joinedload(models.Application.student),
            joinedload(models.Application.scholarship)
        )
        .filter(models.Application.student_id == student_id)
        .all()
    )


# -------------------------------
# Scholarship CRUD
# -------------------------------

def create_scholarship(db: Session, scholarship: schemas.ScholarshipCreate):
    db_scholarship = models.Scholarship(**scholarship.model_dump())
    db.add(db_scholarship)
    db.commit()
    db.refresh(db_scholarship)
    return db_scholarship


def get_scholarships(db: Session):
    return db.query(models.Scholarship).all()


# -------------------------------
# Application CRUD
# -------------------------------

def create_application(db: Session, application: schemas.ApplicationCreate):
    db_application = models.Application(**application.model_dump())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


def get_applications(db: Session):
    return (
        db.query(models.Application)
        .options(
            joinedload(models.Application.student),
            joinedload(models.Application.scholarship)
        )
        .all()
    )


def get_application(db: Session, application_id: int):
    return (
        db.query(models.Application)
        .options(
            joinedload(models.Application.student),
            joinedload(models.Application.scholarship)
        )
        .filter(models.Application.id == application_id)
        .first()
    )


def update_application_status(db: Session, application_id: int, status: str):
    application = db.query(models.Application).filter(
        models.Application.id == application_id
    ).first()

    if application:
        application.status = status
        db.commit()
        db.refresh(application)

    return application


def delete_application(db: Session, application_id: int):
    application = db.query(models.Application).filter(
        models.Application.id == application_id
    ).first()

    if application:
        db.delete(application)
        db.commit()

    return application


# -------------------------------
# Status History CRUD
# -------------------------------

def get_history(db: Session, application_id: int):
    return (
        db.query(models.StatusHistory)
        .filter(models.StatusHistory.application_id == application_id)
        .all()
    )