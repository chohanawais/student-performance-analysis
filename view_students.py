import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print("\n=== ALL Students ====")

for student in students:
    print(
            "ID", student[0],
            "| Name:", student[1],
            "| Marks:", student[2],
            "| City:", student[3]
            )
    connection.close()
