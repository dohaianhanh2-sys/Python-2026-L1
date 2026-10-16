class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def input(self):
        self.__id = input("  Enter Student ID: ").strip()
        self.__name = input("  Enter Student Name: ").strip()
        self.__dob = input("  Enter Date of Birth (DD/MM/YYYY): ").strip()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def describe(self):
        print(f"ID: {self.__id:<10} | Name: {self.__name:<20} | Date of Birth: {self.__dob}")


class Course:
    def __init__(self, course_id="", name=""):
        self.__id = course_id
        self.__name = name

    def input(self):
        self.__id = input("  Enter Course ID: ").strip()
        self.__name = input("  Enter Course Name: ").strip()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def describe(self):
        print(f"ID: {self.__id:<10} | Course Name: {self.__name}")


class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}  # Cấu trúc: {course_id: {student_id: mark}}

    def input_students(self):
        try:
            count = int(input("Enter number of students: "))
            for i in range(count):
                print(f"\n[Student {i + 1}]")
                s = Student()
                s.input()
                self._students.append(s)
        except ValueError:
            print("Invalid input! Number of students must be an integer.")

    def input_courses(self):
        try:
            count = int(input("Enter number of courses: "))
            for i in range(count):
                print(f"\n[Course {i + 1}]")
                c = Course()
                c.input()
                self._courses.append(c)
        except ValueError:
            print("Invalid input! Number of courses must be an integer.")

    def list_students(self):
        if not self._students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for s in self._students:
            s.describe()

    def list_courses(self):
        if not self._courses:
            print("No courses available.")
            return
        print("\n--- Course List ---")
        for c in self._courses:
            c.describe()

    def input_marks(self):
        if not self._courses or not self._students:
            print("Please add both courses and students first.")
            return

        self.list_courses()
        course_id = input("\nEnter Course ID to input marks for: ").strip()

        valid_course = any(c.get_id() == course_id for c in self._courses)
        if not valid_course:
            print("Course ID not found!")
            return

        if course_id not in self._marks:
            self._marks[course_id] = {}

        print(f"\nInputting marks for course {course_id}:")
        for s in self._students:
            while True:
                try:
                    mark = float(input(f"  Enter mark for {s.get_name()} ({s.get_id()}): "))
                    if 0 <= mark <= 20:  # Hoặc thang điểm 10/100 tuỳ quy ước
                        self._marks[course_id][s.get_id()] = mark
                        break
                    else:
                        print("  Mark should be between 0 and 20. Try again.")
                except ValueError:
                    print("  Invalid input! Mark must be a number.")

    def show_marks(self):
        if not self._marks:
            print("No marks recorded yet.")
            return

        self.list_courses()
        course_id = input("\nEnter Course ID to view marks: ").strip()

        if course_id not in self._marks:
            print("No marks recorded for this course.")
            return

        print(f"\n--- Marks for Course {course_id} ---")
        for s in self._students:
            sid = s.get_id()
            mark = self._marks[course_id].get(sid, "N/A")
            print(f"ID: {sid:<10} | Name: {s.get_name():<20} | Mark: {mark}")

    def run(self):
        while True:
            print("\n=== STUDENT MARK MANAGEMENT ===")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks for a course")
            print("6. Show marks for a course")
            print("0. Exit")

            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.input_marks()
            elif choice == "6":
                self.show_marks()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    app = StudentMarkManagement()
    app.run()