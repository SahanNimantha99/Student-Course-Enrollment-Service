from sqlalchemy.orm import Session
from app.models import Course
from fastapi import HTTPException

# Course CRUD operations
def create_course(db: Session, title: str, code: str, capacity: int):
    course = Course(title=title, code=code, capacity=capacity)
    db.add(course)
    try:
        db.commit()
        db.refresh(course)
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="Course code already exists")
    return course

def get_courses(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Course).offset(offset).limit(limit).all()

def get_course_by_id(db: Session, course_id: int):
    course = db.query(Course).get(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
