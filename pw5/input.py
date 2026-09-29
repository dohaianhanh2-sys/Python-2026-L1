from domains.course import Course
from domains.student import Student


def get_students():
  students = []
  n_students = int(input("Enter number of students: "))
  for i in range(n_students):
    print(f"\nStudent {i + 1}:")
    s_id = input("ID: ")
    s_name = input("Name: ")
    s_dob = input("Date of Birth: ")
    students.append(Student(s_id, s_name, s_dob))

  with open("students.txt", "w") as f:
    for s in students:
      f.write(f"{s.id},{s.name},{s.dob}\n")

  return students


def get_courses():
  courses = {}
  n_courses = int(input("\nEnter number of courses: "))
  for i in range(n_courses):
    print(f"\nCourse {i + 1}:")
    c_id = input("Course ID: ")
    c_name = input("Course Name: ")
    c_credits = float(input("Credits: "))
    courses[c_id] = Course(c_id, c_name, c_credits)

  with open("courses.txt", "w") as f:
    for c in courses.values():
      f.write(f"{c.id},{c.name},{c.credits}\n")

  return courses


def get_marks(students, courses):
  with open("marks.txt", "w") as f:
    for c_id, course in courses.items():
      print(f"\n--- Input marks for: {course.name} ({c_id}) ---")
      for s in students:
        raw_score = float(input(f"Mark for {s.name} (ID: {s.id}): "))
        s.add_mark(c_id, raw_score)
        f.write(f"{c_id},{s.id},{s.marks[c_id]}\n")


def load_students():
  students = []
  with open("students.txt", "r") as f:
    for line in f:
      line = line.strip()
      if line:
        s_id, name, dob = line.split(",")
        students.append(Student(s_id, name, dob))
  return students


def load_courses():
  courses = {}
  with open("courses.txt", "r") as f:
    for line in f:
      line = line.strip()
      if line:
        c_id, name, credits = line.split(",")
        courses[c_id] = Course(c_id, name, float(credits))
  return courses


def load_marks(students, courses):
  students_dict = {s.id: s for s in students}
  with open("marks.txt", "r") as f:
    for line in f:
      line = line.strip()
      if line:
        c_id, s_id, score = line.split(",")
        if s_id in students_dict:
          students_dict[s_id].add_mark(c_id, float(score))