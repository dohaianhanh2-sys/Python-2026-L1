from input import get_students, get_courses, get_marks
from output import display_results

def main():
    print("=== DATA INPUT ===")
    students = get_students()
    courses = get_courses()
    get_marks(students, courses)

    for s in students:
        s.calculate_gpa(courses)

    students.sort(key=lambda x: x.gpa, reverse=True)

    display_results(students, courses)

if __name__ == "__main__":
    main()