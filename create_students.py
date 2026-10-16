
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

students = [
    (1, "Ali", 75),
    (2, "Ahmed", 60),
    (3, "Sara", 85),
    (4, "Usman", 40),
    (5, "Ayesha", 90)
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?)",
    students
)

connection.commit()
connection.close()

print("Students table created successfully!")
