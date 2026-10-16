import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT name, marks FROM students")
students = cursor.fetchall()

print("\n=== Student Result Report ===")


for student in students:
    name = student[0]
    marks = student[1]

    if marks >= 50:
        result = "Pass"
    else:
        result = "Fail"
        print("Name:", name, "| Marks:", marks, "| Result:", result)

        connection.close()

