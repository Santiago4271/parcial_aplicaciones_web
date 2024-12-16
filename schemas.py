from pydantic import BaseModel

# Esquemas para Student
class StudentBase(BaseModel):
    name: str
    age: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Grade
class GradeBase(BaseModel):
    student_id: int
    course_id: int
    grade: float

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Enrollment
class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: int

    class Config:
        from_attributes = True