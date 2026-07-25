from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    applications = relationship("Application", back_populates="student")


class Scholarship(Base):
    __tablename__ = "scholarships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

    applications = relationship("Application", back_populates="scholarship")


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    scholarship_id = Column(Integer, ForeignKey("scholarships.id"))
    status = Column(String, nullable=False)
    applied_date = Column(String, nullable=False)

    student = relationship("Student", back_populates="applications")
    scholarship = relationship("Scholarship", back_populates="applications")
    history = relationship("StatusHistory", back_populates="application")


class StatusHistory(Base):
    __tablename__ = "status_history"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id"))
    status = Column(String, nullable=False)
    updated_date = Column(String, nullable=False)

    application = relationship("Application", back_populates="history")