# Student Course Enrollment Service

A small REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** to manage students, courses, and enrollments.

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/SahanNimantha99/Student-Course-Enrollment-Service
cd Student-Course-Enrollment-Service
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment

Windows (Git Bash / WSL):
```bash
source venv/Scripts/activate
```
Windows (CMD):
```bash
venv\Scripts\activate
```
Linux / MacOS:
```bash
source venv/bin/activate
```


### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Configure database

Copy .env.example to .env
```bash
cp .env.example .env
```
Edit .env with your PostgreSQL credentials

### 6. Create tables

Run this once to create tables
```bash
from app.database import Base, engine
from app.models import Student, Course, Enrollment

Base.metadata.create_all(bind=engine)
```

### 7. Start FastAPI server
```bash
uvicorn app.main:app --reload
```
Open Swagger UI: http://127.0.0.1:8000/docs


## Example API Requests and Responses

1. Create Student
```bash
curl -X POST "http://127.0.0.1:8000/create-student" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"full_name": "Sahan Nimantha", "email": "sahan@example.com"}'
```
Response :
```bash
{
  "id": 1,
  "full_name": "Sahan Nimantha",
  "email": "sahan@example.com",
  "created_at": "2026-02-13T09:09:04.820958"
}
```

2. Test duplicate email:
```bash
curl -X POST "http://127.0.0.1:8000/create-student" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"full_name": "Sahan Nimantha 2", "email": "sahan@example.com"}'
```
Response :
```bash
{
  "detail": "Email already exists"
}
```

1. Create Course
```bash
curl -X POST "http://127.0.0.1:8000/create-course" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"title": "Mathematics 101", "code": "MATH101", "capacity": 4}'
```
Response :
```bash
{
  "id": 3,
  "title": "Mathematics 101",
  "code": "MATH101",
  "capacity": 4,
  "created_at": "2026-02-13T09:15:51.636282"
}
```

2. Test duplicate course code:
```bash
curl -X POST "http://127.0.0.1:8000/create-course" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"title": "Mathematics 101", "code": "MATH101", "capacity": 4}'
```
Response:
```bash
{
  "detail": "Course code already exists"
}

```


1. List Students / Courses
Get Students :
```bash
curl -X GET "http://127.0.0.1:8000/get-students?offset=0&limit=10" -H "accept: application/json"
```
Response:
```bash
[
  {
    "id": 1,
    "full_name": "Sahan Nimantha",
    "email": "sahan@example.com",
    "created_at": "2026-02-13T09:09:04.820958"
  }
]
```

Get Courses :
```bash
curl -X GET "http://127.0.0.1:8000/get-courses?offset=0&limit=10" -H "accept: application/json"
```
Response:
```bash
[
  {
    "id": 1,
    "title": "Computer Science 101",
    "code": "CS101",
    "capacity": 2,
    "created_at": "2026-02-13T09:12:33.103589"
  },
  {
    "id": 3,
    "title": "Mathematics 101",
    "code": "MATH101",
    "capacity": 4,
    "created_at": "2026-02-13T09:15:51.636282"
  }
]
```



1. Get Student / Course by ID
Get Student :
```bash
curl -X GET "http://127.0.0.1:8000/get-student-by-id/1" -H "accept: application/json"
```
Response:
```bash
{
  "id": 1,
  "full_name": "Sahan Nimantha",
  "email": "sahan@example.com",
  "created_at": "2026-02-13T09:09:04.820958"
}
```

Get Course :
```bash
curl -X GET "http://127.0.0.1:8000/get-course-by-id/1" -H "accept: application/json"
```
Response:
```bash
{
  "id": 1,
  "title": "Computer Science 101",
  "code": "CS101",
  "capacity": 2,
  "created_at": "2026-02-13T09:12:33.103589"
}
```

1. Enroll Student in Course
```bash
curl -X POST "http://127.0.0.1:8000/enrollment-student" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"student_id": 1, "course_id": 1}'
```
Response:

```bash
{
  "id": 1,
  "student_id": 1,
  "course_id": 1,
  "status": "active",
  "enrolled_at": "2026-02-13T09:20:59.093336",
  "created_at": "2026-02-13T09:20:59.093336"
}
```




2. Test duplicate enrollment:
```bash
curl -X POST "http://127.0.0.1:8000/enrollment-student" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"student_id": 1, "course_id": 1}'
```
Response:

```bash
{
  "detail": "Student already enrolled in this course"
}
```

1. List Enrollments
```bash
curl -X GET "http://127.0.0.1:8000/get-enrollments" -H "accept: application/json"
```
Response:
```bash
[
  {
    "id": 1,
    "student_id": 1,
    "course_id": 1,
    "status": "active",
    "enrolled_at": "2026-02-13T09:20:59.093336",
    "created_at": "2026-02-13T09:20:59.093336"
  }
]
```

1. Cancel Enrollment
```bash
curl -X PATCH "http://127.0.0.1:8000/cancel-enrollment/1" -H "accept: application/json"
```
Response:
```bash
{
  "message": "Enrollment cancelled"
}
```

