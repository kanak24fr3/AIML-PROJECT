import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

subjects = ["Math", "Physics", "CS"]

# Add Total & Percentage
df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = df["Total"] / len(subjects)

# Rank students (1 = highest)
df["Rank"] = df["Total"].rank(ascending=False, method='min')

# Sort by rank
df = df.sort_values(by="Rank")

print("\n Student Rankings:\n")
print(df[["Name", "Total", "Percentage", "Rank"]])

# 🥇 Get topper
topper = df.iloc[0]
print(f"\n Topper: {topper['Name']} with {topper['Total']} marks")

# Horizontal Bar Chart: Total Marks
plt.figure(figsize=(8,5))

colors = ["gold" if name == topper["Name"] else "skyblue" for name in df["Name"]]

plt.barh(df["Name"], df["Total"], color=colors)

plt.title("Student Total Marks (Topper Highlighted)")
plt.xlabel("Total Marks")
plt.ylabel("Students")

plt.gca().invert_yaxis()  # Top rank at top
plt.tight_layout()
plt.show()

# Subject-wise Highest Scorer
highest_each_subject = {}

for sub in subjects:
    topper_sub = df.loc[df[sub].idxmax()]
    highest_each_subject[sub] = topper_sub["Name"]

print("\n Subject-wise Toppers:")
for sub, name in highest_each_subject.items():
    print(f"{sub}: {name}")

#  Pie Chart: Class Contribution (Total Marks Share)
plt.figure(figsize=(6,6))
plt.pie(df["Total"], labels=df["Name"], autopct='%1.1f%%')
plt.title("Contribution to Total Class Marks")
plt.tight_layout()
plt.show()