import os
import sqlite3
from dotenv import load_dotenv

# Load environment variables from.env file
load_dotenv()

# Get the value of the DATABASE_URL environment variable
DATABASE_PATH = os.getenv("DATABASE_PATH")

# Sets the directory and full path to the database 
DB_FOLDER = "repositories"
DB_PATH = os.path.join(DB_FOLDER, "book.db")

#Create folder if not exist
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

# Connect to the SQLite database
conn = sqlite3.connect("book.db")

# Cursor object to execute SQL queries
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL CHECK (name <> ''), 
    age INTEGER NOT NULL CHECK (age > 0), 
    gender TEXT NOT NULL CHECK (gender <> ''), 
    id_doc VARCHAR(20) UNIQUE NOT NULL CHECK (LENGTH(id_doc) <= 20 AND id_doc <> ''), 
    class_student TEXT NOT NULL CHECK (class_student <> ''))
    """)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()