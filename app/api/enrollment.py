from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import EnrollmentCreate
from app.crud.enrollment import enroll_student
from app.models import Enrollment

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Enrollment endpoints
@router.post("/enrollment-student", status_code=201)
def enroll(data: EnrollmentCreate, db: Session = Depends(get_db)):
    return enroll_student(db, data.student_id, data.course_id)

@router.get("/get-enrollments")
def list_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()

@router.patch("/cancel-enrollment/{enrollment_id}")
def cancel(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = db.query(Enrollment).get(enrollment_id)
    if not enrollment:
        return {"error": "Enrollment not found"}
    enrollment.status = "cancelled"
    db.commit()
    return {"message": "Enrollment cancelled"}
