import pandas as pd


data = {
        "Name": ["Ali", "Ahmed", "Sara", "Fatima", "Usman"],
        "Marks": [75, 88, 92, 64, 45],
        "City": ["Sargodha", "Khushab", "Lahore", "Islamabad", "Sargodha"]
        }

df = pd.DataFrame(data)

print("=== Student Report ===")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Hightest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())


print("\n=== Pass Students ===")
print(df.loc[df["Marks"].idxmax()])

