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