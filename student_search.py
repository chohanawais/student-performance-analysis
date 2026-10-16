import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

name = input("Enter student name: ")

cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
        )

rows = cursor.fetchall()

if rows:
    print("\nStudent Found:")
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Marks:", row[2])
    else:

        print("Student not found!")

        connection.close()
