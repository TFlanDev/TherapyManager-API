import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
print("DEBUG:", os.getenv("DATABASE_URL"))
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(engine)
Base = DeclarativeBase()
class Base(DeclarativeBase):
    pass

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close