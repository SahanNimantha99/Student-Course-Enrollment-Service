from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import StudentCreate
from app.crud.student import create_student, get_students, get_student_by_id

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Student endpoints
@router.post("/create-student", status_code=201)
def create(data: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, data.full_name, data.email)

@router.get("/get-students")
def list_students(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_students(db, offset, limit)

@router.get("/get-student-by-id/{student_id}")
def get_by_id(student_id: int, db: Session = Depends(get_db)):
    return get_student_by_id(db, student_id)
