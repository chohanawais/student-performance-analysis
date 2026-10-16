import sqlite3
import pandas as pd

connection = sqlite3.connect("students.db")

df = pd.read_sql_query(
        "SELECT * FROM students",

         connection
)

print("=== Student Database ===")
print(df)


print("\nAverage Marks:")
print(df["marks"].mean())


print("\nHighest Marks:")
print(df["marks"].max())

print("\nLowest Marks:")
print(df["marks"].min())

print("\n== Students Who Passed ===")
print(df[df["marks"] >= 50])


connection.close()
