import gzip
import os
import pickle
from input import get_courses, get_marks, get_students
from output import display_results

# Nếu bạn muốn dùng phần Extra
try:
  from extra import export_csv, query_data
except ImportError:
  pass


def save_pickled_data(students, courses):
  """Nén và lưu trực tiếp dữ liệu đối tượng vào students.dat bằng pickle."""
  data = {"students": students, "courses": courses}
  with gzip.open("students.dat", "wb") as f:
    pickle.dump(data, f)
  print("Data pickled, compressed and saved to students.dat.")


def load_pickled_data():
  """Giải nén và đọc dữ liệu đối tượng từ students.dat."""
  with gzip.open("students.dat", "rb") as f:
    data = pickle.load(f)
  return data["students"], data["courses"]


def main():
  if os.path.exists("students.dat"):
    print("Found existing students.dat. Decompressing and loading data...")
    students, courses = load_pickled_data()
  else:
    print("No existing data found. Please enter fresh data.")
    students = get_students()
    courses = get_courses()
    get_marks(students, courses)

  for s in students:
    s.calculate_gpa(courses)

  students.sort(key=lambda x: x.gpa, reverse=True)

  display_results(students, courses)

  # Lưu dữ liệu sang pickle nén
  save_pickled_data(students, courses)

  # --- PHẦN EXTRA (CSV & PANDAS QUERY) ---
  run_extra = input("\nDo you want to run Extra task (CSV & Query)? (y/n): ")
  if run_extra.strip().lower() == "y":
    try:
      export_csv(students, courses)
      query_data()
    except Exception as e:
      print(f"Extra task error: {e}")


if __name__ == "__main__":
  main()