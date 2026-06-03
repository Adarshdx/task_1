import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Raw Dataset
data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name": ["Aman", "Priya", "Rahul", "Neha", "Karan", "Anjali", "Rohit", "Simran"],
    "Age": [19, 20, 19, 21, 20, 19, 20, 21],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Maths": [78, 88, None, 92, 65, 85, 120, 80],
    "Science": [82, 90, 76, 95, 68, 88, 70, 85],
    "English": [75, 85, 70, 89, None, 90, 72, 83]
}

df = pd.DataFrame(data)

print("===== ORIGINAL DATASET =====")
print(df)

# Handle missing values
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

# Remove outliers (Maths > 100)
df = df[df["Maths"] <= 100]

# Remove duplicates
df = df.drop_duplicates()

print("\n===== CLEANED DATASET =====")
print(df)

# Save cleaned dataset
df.to_csv("output/cleaned_student_data.csv", index=False)

# -----------------------------
# Visualization 1: Bar Chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Maths"])
plt.title("Maths Scores of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/maths_scores.png")
plt.close()

# -----------------------------
# Visualization 2: Pie Chart
# -----------------------------
avg_scores = [
    df["Maths"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

subjects = ["Maths", "Science", "English"]

plt.figure(figsize=(6, 6))
plt.pie(avg_scores, labels=subjects, autopct="%1.1f%%")
plt.title("Average Subject Performance")
plt.savefig("output/subject_performance.png")
plt.close()

# -----------------------------
# Visualization 3: Line Chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["Name"], df["Science"], marker="o")
plt.title("Science Marks Trend")
plt.xlabel("Students")
plt.ylabel("Science Marks")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/science_trend.png")
plt.close()

print("\nProject Completed Successfully!")
print("Files Generated:")
print("1. output/cleaned_student_data.csv")
print("2. output/maths_scores.png")
print("3. output/subject_performance.png")
print("4. output/science_trend.png")