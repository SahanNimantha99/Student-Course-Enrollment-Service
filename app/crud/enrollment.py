from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Enrollment, Course

# Enrollment CRUD operations
def enroll_student(db: Session, student_id: int, course_id: int):
    course = db.query(Course).get(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    active_count = db.query(Enrollment).filter(
        Enrollment.course_id == course_id,
        Enrollment.status == "active"
    ).count()

    if active_count >= course.capacity:
        raise HTTPException(status_code=400, detail="Course capacity reached")

    existing = db.query(Enrollment).filter_by(
        student_id=student_id,
        course_id=course_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")

    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment
