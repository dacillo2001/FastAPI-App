# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Load the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("postgresql://dbname_re6j_user:HlBY5FpYoVjXlBUNS4bQBpLMzEqsZ1zj@dpg-cvv3q6adbo4c73fdt44g-a:5432/dbname_re6j")

# Set up the database connection
engine = create_engine(DATABASE_URL)

# Set up the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()
