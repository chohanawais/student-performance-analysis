import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


connection = sqlite3.connect("students.db")

df = pd.read_sql_query(
        "SELECT name, marks FROM students", 
        connection
        )

connection.close()

print(df)

plt.bar(df["name"], df["marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.ylim(0, 100)
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("student_marks.png")
print("Graph saved as student_marks.png")
