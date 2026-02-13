from fastapi import FastAPI
from app.database import Base, engine
from app.api import student, course, enrollment

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Course Enrollment Service")

app.include_router(student.router)
app.include_router(course.router)
app.include_router(enrollment.router)
