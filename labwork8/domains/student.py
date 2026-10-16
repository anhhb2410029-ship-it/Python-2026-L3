import math
import numpy as np
from .person import Person

class Student(Person):
    def __init__(self, pid, name, dob):
        super().__init__(pid, name, dob)
        self.__marks = {}
        self.__gpa = 0.0

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(mark * 10) / 10

    def calculate_gpa(self, courses):
        marks_list = []
        credits_list = []
        for cid, mark in self.__marks.items():
            course = next((c for c in courses if c.get_id() == cid), None)
            if course:
                marks_list.append(mark)
                credits_list.append(course.get_credits())
        
        if credits_list:
            marks_arr = np.array(marks_list)
            credits_arr = np.array(credits_list)
            self.__gpa = np.average(marks_arr, weights=credits_arr)
        else:
            self.__gpa = 0.0

    def get_gpa(self):
        return self.__gpa