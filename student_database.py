import sqlite3

connection = sqlite3.connect("Student.db")
cursor = connection.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT,
        marks IMTEGER,
        city TEXT
        )
        """)

students = [
        ("Ali", 75, "Sargodha"),
        ("Ahmed", 88, "Khushab"),
        ("Sara", 92, "Lahore"),
        ("Fatima", 64, "Islamabad"),
        ("Usman", 45, "Sargodha")
        ]

cursor.executemany("""
        INSERT INTO students (name, marks, city)
        VALUES (?, ?, ?)
        """, students)

connection.commit()

print("Students saved successfully!")

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

    connection.close()
