from pydantic import BaseModel


# ---------- Student ----------

class StudentBase(BaseModel):
    name: str
    department: str
    year: int


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Scholarship ----------

class ScholarshipBase(BaseModel):
    name: str
    amount: int


class ScholarshipCreate(ScholarshipBase):
    pass


class Scholarship(ScholarshipBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Application ----------

class ApplicationBase(BaseModel):
    student_id: int
    scholarship_id: int
    status: str
    applied_date: str


class ApplicationCreate(ApplicationBase):
    pass


class Application(ApplicationBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Status History ----------

class StatusHistoryBase(BaseModel):
    application_id: int
    status: str
    updated_date: str


class StatusHistoryCreate(StatusHistoryBase):
    pass


class StatusHistory(StatusHistoryBase):
    id: int

    class Config:
        from_attributes = True