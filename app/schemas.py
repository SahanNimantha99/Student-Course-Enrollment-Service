from pydantic import BaseModel, EmailStr
from typing import Optional

# Student Schemas
class StudentCreate(BaseModel):
    full_name: str
    email: EmailStr

class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True


# Course Schemas
class CourseCreate(BaseModel):
    title: str
    code: str
    capacity: Optional[int] = 30

class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True


# Enrollment Schemas
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
