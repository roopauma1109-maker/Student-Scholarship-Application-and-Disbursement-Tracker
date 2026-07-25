from database import SessionLocal, engine
from models import Base, Student, Scholarship, Application

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ----------------------------
# Students
# ----------------------------

students = [
    Student(name="Roopa", department="CSE", year=4),
    Student(name="Arun", department="IT", year=3),
    Student(name="Priya", department="ECE", year=2),
    Student(name="Kavin", department="CSE", year=4),
    Student(name="Meena", department="EEE", year=3),
]

db.add_all(students)
db.commit()

# ----------------------------
# Scholarships
# ----------------------------

scholarships = [
    Scholarship(name="Merit Scholarship", amount=50000),
    Scholarship(name="Sports Scholarship", amount=30000),
]

db.add_all(scholarships)
db.commit()

# ----------------------------
# Applications
# ----------------------------

applications = [
    Application(
        student_id=1,
        scholarship_id=1,
        status="Submitted",
        applied_date="2026-07-20"
    ),
    Application(
        student_id=2,
        scholarship_id=2,
        status="Verified",
        applied_date="2026-07-18"
    ),
    Application(
        student_id=3,
        scholarship_id=1,
        status="Approved",
        applied_date="2026-07-15"
    ),
]

db.add_all(applications)
db.commit()

db.close()

print("Sample data inserted successfully!")