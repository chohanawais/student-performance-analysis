
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT name, marks FROM students")
students = cursor.fetchall()

print("\n=== Student Performance Analysis ===")

if students:
    total_marks = 0

    for student in students:
        name = student[0]
        marks = student[1]
        total_marks += marks

        print("Name:", name, "| Marks:", marks)

    average = total_marks / len(students)

    print("\nTotal Students:", len(students))
    print("Average Marks:", round(average, 2))
else:
    print("No student records found.")

connection.close()

