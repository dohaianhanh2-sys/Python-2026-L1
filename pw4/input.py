from domains.student import Student
from domains.course import Course

def get_students():
    students = []
    n_students = int(input("Enter number of students: "))
    for i in range(n_students):
        print(f"\nStudent {i + 1}:")
        s_id = input("ID: ")
        s_name = input("Name: ")
        s_dob = input("Date of Birth: ")
        students.append(Student(s_id, s_name, s_dob))
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
    return courses

def get_marks(students, courses):
    for c_id, course in courses.items():
        print(f"\n--- Input marks for: {course.name} ({c_id}) ---")
        for s in students:
            raw_score = float(input(f"Mark for {s.name} (ID: {s.id}): "))
            s.add_mark(c_id, raw_score)