from sqlalchemy.orm import Session
import models
import re


def get_response(question: str, db: Session):

    question = question.lower().strip()
    question = re.sub(r"[^\w\s]", "", question)

    # Rejected Applications
    if "rejected" in question:
        count = (
            db.query(models.Application)
            .filter(models.Application.status == "Rejected")
            .count()
        )
        return f"Rejected applications: {count}"

    # Approved Applications
    elif "approved" in question and "status" not in question:
        count = (
            db.query(models.Application)
            .filter(models.Application.status == "Approved")
            .count()
        )
        return f"Approved applications: {count}"

    # Verified Applications
    elif "verified" in question:
        count = (
            db.query(models.Application)
            .filter(models.Application.status == "Verified")
            .count()
        )
        return f"Verified applications: {count}"

    # Submitted Applications
    elif "submitted" in question:
        count = (
            db.query(models.Application)
            .filter(models.Application.status == "Submitted")
            .count()
        )
        return f"Submitted applications: {count}"

    # Student Application Status
    elif (
        "status" in question
        or "track" in question
        or "application status" in question
    ):

        students = db.query(models.Student).all()

        for student in students:
            if student.name.lower() in question:

                application = (
                    db.query(models.Application)
                    .filter(models.Application.student_id == student.id)
                    .first()
                )

                if application:
                    return f"{student.name}'s application is {application.status}"

        return "Student not found."

    # Total Applications
    elif (
        "total applications" in question
        or "application count" in question
        or "how many applications" in question
        or "total number of applications" in question
    ):
        count = db.query(models.Application).count()
        return f"Total applications: {count}"

    return "Sorry, I don't understand that question."