from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, default=30)
    created_at = Column(DateTime, server_default=func.now())


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    status = Column(String, default="active")
    enrolled_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        # no duplicate enrollments for same student and course
        UniqueConstraint("student_id", "course_id", name="uq_student_course"),
    )
