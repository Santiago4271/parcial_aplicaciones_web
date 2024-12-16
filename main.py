from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .database import database
from .crud import create_student, get_students, get_student, update_student, delete_student, create_grade, get_grades, get_grade, update_grade, delete_grade, create_enrollment, get_enrollments, delete_enrollment
from .schemas import StudentCreate, Student, GradeCreate, Grade, EnrollmentCreate, Enrollment

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:5173",  # Añade aquí la URL de tu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Rutas para Student
@app.post("/students/", response_model=Student)
async def create_student_endpoint(student: StudentCreate):
    return await create_student(student)

@app.get("/students/", response_model=List[Student])
async def get_students_endpoint():
    return await get_students()

@app.get("/students/{student_id}", response_model=Student)
async def get_student_endpoint(student_id: int):
    student = await get_student(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=Student)
async def update_student_endpoint(student_id: int, student: StudentCreate):
    return await update_student(student_id, student)

@app.delete("/students/{student_id}")
async def delete_student_endpoint(student_id: int):
    await delete_student(student_id)
    return {"message": "Student deleted successfully"}

# Rutas para Grade
@app.post("/grades/", response_model=Grade)
async def create_grade_endpoint(grade: GradeCreate):
    return await create_grade(grade)

@app.get("/grades/", response_model=List[Grade])
async def get_grades_endpoint():
    return await get_grades()

@app.get("/grades/{grade_id}", response_model=Grade)
async def get_grade_endpoint(grade_id: int):
    grade = await get_grade(grade_id)
    if grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return grade

@app.put("/grades/{grade_id}", response_model=Grade)
async def update_grade_endpoint(grade_id: int, grade: GradeCreate):
    return await update_grade(grade_id, grade)

@app.delete("/grades/{grade_id}")
async def delete_grade_endpoint(grade_id: int):
    await delete_grade(grade_id)
    return {"message": "Grade deleted successfully"}

# Rutas para Enrollment
@app.post("/enrollments/", response_model=Enrollment)
async def create_enrollment_endpoint(enrollment: EnrollmentCreate):
    return await create_enrollment(enrollment)

@app.get("/enrollments/", response_model=List[Enrollment])
async def get_enrollments_endpoint():
    return await get_enrollments()

@app.delete("/enrollments/{enrollment_id}")
async def delete_enrollment_endpoint(enrollment_id: int):
    await delete_enrollment(enrollment_id)
    return {"message": "Enrollment deleted successfully"}