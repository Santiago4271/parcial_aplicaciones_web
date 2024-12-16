# backend/database.py
from databases import Database
from sqlalchemy import create_engine, MetaData

# URL de conexión a SQLite
DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})