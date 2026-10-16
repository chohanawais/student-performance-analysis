import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect("students.db")


df = pd.read_sql_query(
        "SELECT name, marks FROM students",
        connection
        )

connection.close()

plt.figure(figsize=(10, 5))


plt.bar(df["name"], df["marks"])


plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")


plt.ylim(0, 100)
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("performance_graph.png")

print("Graph saved successfullly: performance_graph.png")
