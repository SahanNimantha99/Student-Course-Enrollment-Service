from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import CourseCreate
from app.crud.course import create_course, get_courses, get_course_by_id

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Course endpoints
@router.post("/create-course", status_code=201)
def create(data: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db, data.title, data.code, data.capacity)

@router.get("/get-courses")
def list_courses(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_courses(db, offset, limit)

@router.get("/get-course-by-id/{course_id}")
def get_by_id(course_id: int, db: Session = Depends(get_db)):
    return get_course_by_id(db, course_id)
