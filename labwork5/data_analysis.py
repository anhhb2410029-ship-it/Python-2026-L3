44

import pandas as pd

print("=== PART 1: DATA MANIPULATION ===")

students = pd.read_csv('students.csv')

print("First five rows:\n", students.head())

rows, cols = students.shape
print(f"\nNumber of rows: {rows}, columns: {cols}")

print("\nName and GPA:\n", students[['name', 'GPA']].head())

good_students = students[students['GPA'] >= 3.5]
print("\nStudents with GPA >= 3.5:\n", good_students[['name', 'GPA']])

students_sorted = students.sort_values(by='GPA', ascending=False)
print("\nStudents sorted by GPA:\n", students_sorted[['name', 'GPA']])


major_gpa = students.groupby('major')['GPA'].mean()
print("\nAverage GPA by major:\n", major_gpa)


print("\n\n=== PART 2: FROM RAW DATA TO USEFUL INFO ===")

scores = pd.read_csv('scores.csv')

print("Missing values in students.csv:\n", students.isnull().sum())
print("\nMissing values in scores.csv:\n", scores.isnull().sum())


students = students.dropna()
scores = scores.dropna()

data = pd.merge(students, scores, on='student_id')


data['average_score'] = data[['python', 'math', 'database']].mean(axis=1)

top_students = data.sort_values(
    by='average_score', ascending=False
).head(5)

print("\nTop 5 students:\n", top_students[
    ['student_id', 'name', 'major', 'average_score']
])

major_score = data.groupby('major')['average_score'].mean()
print("\nAverage score by major:\n", major_score)