import sqlite3

connection = sqlite3.connect("/home/cchohan/data-science/project1/students.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        marks INTEGER,
        city TEXT
)
""")



name = input("Enter student name: ")
marks = int(input("Enter student marks: "))
city = input("Enter student city: ")


cursor.execute("""
        INSERT INTO students (name, marks, city)
        VALUES (?, ?, ?)
        """,(name, marks, city))


connection.commit()

print("\nStudent added successfully!")

cursor.execute("SELECT * FROM students ORDER BY id DESC LIMIT 1")
print(cursor.fetchone())

connection.close()
