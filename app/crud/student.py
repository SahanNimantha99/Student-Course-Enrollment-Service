from sqlalchemy.orm import Session
from app.models import Student
from fastapi import HTTPException

# Student CRUD operations
def create_student(db: Session, full_name: str, email: str):
    student = Student(full_name=full_name, email=email)
    db.add(student)
    try:
        db.commit()
        db.refresh(student)
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")
    return student

def get_students(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Student).offset(offset).limit(limit).all()

def get_student_by_id(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
