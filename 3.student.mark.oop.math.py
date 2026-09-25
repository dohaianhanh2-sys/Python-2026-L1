import curses
import math
import numpy as np


class Student:

  def __init__(self, s_id, name, dob):
    self.id = s_id
    self.name = name
    self.dob = dob
    self.marks = {}
    self.gpa = 0.0

  def add_mark(self, course_id, score):
    self.marks[course_id] = math.floor(score * 10) / 10

  def calculate_gpa(self, courses_dict):
    scores = []
    credits = []

    for c_id, score in self.marks.items():
      if c_id in courses_dict:
        scores.append(score)
        credits.append(courses_dict[c_id].credits)

    if len(scores) == 0:
      self.gpa = 0.0
      return self.gpa

    scores_arr = np.array(scores)
    credits_arr = np.array(credits)

    self.gpa = float(np.average(scores_arr, weights=credits_arr))
    return self.gpa


class Course:

  def __init__(self, c_id, name, credits):
    self.id = c_id
    self.name = name
    self.credits = credits


def get_user_input():
  students = []
  courses = {}

  print("DATA INPUT")
  n_students = int(input("Enter number of students: "))
  for i in range(n_students):
    print(f"\nStudent {i + 1}:")
    s_id = input("ID: ")
    s_name = input("Name: ")
    s_dob = input("Date of Birth: ")
    students.append(Student(s_id, s_name, s_dob))

  n_courses = int(input("\nEnter number of courses: "))
  for i in range(n_courses):
    print(f"\nCourse {i + 1}:")
    c_id = input("Course ID: ")
    c_name = input("Course Name: ")
    c_credits = float(input("Credits: "))
    courses[c_id] = Course(c_id, c_name, c_credits)

  for c_id, course in courses.items():
    print(f"\nInput marks for: {course.name} ({c_id})")
    for s in students:
      raw_score = float(input(f"Mark for {s.name} (ID: {s.id}): "))
      s.add_mark(c_id, raw_score)

  for s in students:
    s.calculate_gpa(courses)

  students.sort(key=lambda x: x.gpa, reverse=True)

  return students, courses


def draw_curses_ui(stdscr, students, courses):
  curses.curs_set(0)
  stdscr.clear()

  max_y, max_x = stdscr.getmaxyx()

  def safe_addstr(y, x, text, attr=curses.A_NORMAL):
    if y < max_y - 1 and x < max_x:
      stdscr.addstr(y, x, text[: max_x - x - 1], attr)

  line = 1
  safe_addstr(line, 2, "COURSE LIST", curses.A_BOLD)
  line += 1
  for c in courses.values():
    safe_addstr(line, 4, f"- {c.id}: {c.name} ({c.credits} credits)")
    line += 1

  line += 1
  safe_addstr(
      line, 2, "STUDENT RANKING BY GPA", curses.A_BOLD
  )
  line += 1
  header = (
      f"{'Student ID':<12} | {'Name':<20} | {'Date of Birth':<15} | {'GPA':<6}"
  )
  safe_addstr(line, 4, header, curses.A_UNDERLINE)
  line += 1

  for s in students:
    row = f"{s.id:<12} | {s.name:<20} | {s.dob:<15} | {s.gpa:<6.2f}"
    safe_addstr(line, 4, row)
    line += 1

  safe_addstr(line + 1, 2, "Press any key to exit...", curses.A_DIM)
  stdscr.refresh()
  stdscr.getch()


def main():
  students, courses = get_user_input()
  curses.wrapper(lambda stdscr: draw_curses_ui(stdscr, students, courses))


if __name__ == "__main__":
  main()