import csv
import pandas as pd

def export_csv(students, courses):
  with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "dob", "gpa"])
    for s in students:
      writer.writerow([s.id, s.name, s.dob, s.gpa])

  with open("courses.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "credits"])
    for c in courses.values():
      writer.writerow([c.id, c.name, c.credits])

  with open("marks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["course_id", "student_id", "mark"])
    for s in students:
      for c_id, mark in s.marks.items():
        writer.writerow([c_id, s.id, mark])

  print("Exported to students.csv, courses.csv, and marks.csv successfully.")


def query_data():
  try:
    df = pd.read_csv("students.csv")
    print("\n--- Students Table ---")
    print(df)

    cond = input(
        '\nEnter query condition (e.g. name == "Mr. Volunteers" or gpa >= 10): '
    )
    if cond.strip():
      result = df.query(cond)
      print("\n--- Query Result ---")
      print(result)

  except Exception as e:
    print(f"Error querying data: {e}")