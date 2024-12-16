# backend/models.py
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from .database import metadata

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer, nullable=False),
    Column("email", String, nullable=False, unique=True),
)

courses = Table(
    "courses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
)

enrollments = Table(
    "enrollments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id")),
)