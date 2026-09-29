import os
import zipfile
from input import (
    get_courses,
    get_marks,
    get_students,
    load_courses,
    load_marks,
    load_students,
)
from output import display_results


def compress_files():
  data_files = ["students.txt", "courses.txt", "marks.txt"]
  with zipfile.ZipFile(
      "students.dat", "w", compression=zipfile.ZIP_DEFLATED
  ) as archive:
    for filename in data_files:
      if os.path.exists(filename):
        archive.write(filename)
        os.remove(filename)


def decompress_data():
  with zipfile.ZipFile("students.dat", "r") as archive:
    archive.extractall()


def main():
  if os.path.exists("students.dat"):
    print("Found existing students.dat. Decompressing and loading data...")
    decompress_data()
    students = load_students()
    courses = load_courses()
    load_marks(students, courses)
  else:
    print("No existing data found. Please enter fresh data.")
    students = get_students()
    courses = get_courses()
    get_marks(students, courses)

  for s in students:
    s.calculate_gpa(courses)

  students.sort(key=lambda x: x.gpa, reverse=True)

  display_results(students, courses)

  compress_files()
  print("Data compressed and saved to students.dat.")


if __name__ == "__main__":
  main()