from .database import database
from .schemas import StudentCreate, Student, GradeCreate, Grade, EnrollmentCreate, Enrollment

# Funciones CRUD para Student
async def create_student(student: StudentCreate):
    query = """
    INSERT INTO students (name, age)
    VALUES (:name, :age)
    RETURNING id
    """
    values = {
        "name": student.name,
        "age": student.age
    }
    student_id = await database.execute(query=query, values=values)
    return {**student.dict(), "id": student_id}

async def get_students():
    query = "SELECT * FROM students"
    return await database.fetch_all(query=query)

async def get_student(student_id: int):
    query = "SELECT * FROM students WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": student_id})

async def update_student(student_id: int, student: StudentCreate):
    query = """
    UPDATE students
    SET name = :name, age = :age
    WHERE id = :id
    """
    values = {
        "id": student_id,
        "name": student.name,
        "age": student.age
    }
    await database.execute(query=query, values=values)
    return {**student.dict(), "id": student_id}

async def delete_student(student_id: int):
    query = "DELETE FROM students WHERE id = :id"
    await database.execute(query=query, values={"id": student_id})
    return {"message": "Student deleted successfully"}

# Funciones CRUD para Grade
async def create_grade(grade: GradeCreate):
    query = """
    INSERT INTO grades (student_id, course_id, grade)
    VALUES (:student_id, :course_id, :grade)
    RETURNING id
    """
    values = {
        "student_id": grade.student_id,
        "course_id": grade.course_id,
        "grade": grade.grade
    }
    grade_id = await database.execute(query=query, values=values)
    return {**grade.dict(), "id": grade_id}

async def get_grades():
    query = "SELECT * FROM grades"
    return await database.fetch_all(query=query)

async def get_grade(grade_id: int):
    query = "SELECT * FROM grades WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": grade_id})

async def update_grade(grade_id: int, grade: GradeCreate):
    query = """
    UPDATE grades
    SET student_id = :student_id, course_id = :course_id, grade = :grade
    WHERE id = :id
    """
    values = {
        "id": grade_id,
        "student_id": grade.student_id,
        "course_id": grade.course_id,
        "grade": grade.grade
    }
    await database.execute(query=query, values=values)
    return {**grade.dict(), "id": grade_id}

async def delete_grade(grade_id: int):
    query = "DELETE FROM grades WHERE id = :id"
    await database.execute(query=query, values={"id": grade_id})
    return {"message": "Grade deleted successfully"}

# Funciones CRUD para Enrollment
async def create_enrollment(enrollment: EnrollmentCreate):
    query = """
    INSERT INTO enrollments (student_id, course_id)
    VALUES (:student_id, :course_id)
    RETURNING id
    """
    values = {
        "student_id": enrollment.student_id,
        "course_id": enrollment.course_id
    }
    enrollment_id = await database.execute(query=query, values=values)
    return {**enrollment.dict(), "id": enrollment_id}

async def get_enrollments():
    query = "SELECT * FROM enrollments"
    return await database.fetch_all(query=query)

async def delete_enrollment(enrollment_id: int):
    query = "DELETE FROM enrollments WHERE id = :id"
    await database.execute(query=query, values={"id": enrollment_id})
    return {"message": "Enrollment deleted successfully"}