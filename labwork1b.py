students = []
courses = []
marks = {}

n_students = int(input("Enter number of students: "))
for i in range(n_students):
    print(f"\nStudent {i + 1}:")
    s_id = input("ID: ")
    s_name = input("Name: ")
    s_dob = input("Date of Birth: ")
    students.append({"id": s_id, "name": s_name, "dob": s_dob})

n_courses = int(input("\nEnter number of courses: "))
for i in range(n_courses):
    print(f"\nCourse {i + 1}:")
    c_id = input("Course ID: ")
    c_name = input("Course Name: ")
    courses.append({"id": c_id, "name": c_name})

print("\nCOURSE LIST")
for c in courses:
    print(c["id"], "-", c["name"])

print("\nSTUDENT LIST")
for s in students:
    print(s["id"], "-", s["name"], "-", s["dob"])


target_course = input("\nEnter course ID to input marks: ")
marks[target_course] = {}

print(f"Enter marks for course {target_course}:")
for s in students:
    score = float(input(f"Mark for {s['name']} (ID: {s['id']}): "))
    marks[target_course][s["id"]] = score


print(f"\nMARKS FOR {target_course} COURSE")
for s in students:
    s_id = s["id"]
    diem = marks[target_course][s_id]
    print(s["name"], f"({s_id}):", diem)