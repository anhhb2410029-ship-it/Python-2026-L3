import math
import numpy as np
import curses

class Person:
    def __init__(self, pid, name, dob):
        self._id = pid
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

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

class Course:
    def __init__(self, cid, name, credits):
        self._id = cid
        self._name = name
        self._credits = credits

    def get_id(self):
        return self._id
        
    def get_credits(self):
        return self._credits

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def get_input(self, stdscr, prompt, row):
        stdscr.addstr(row, 0, prompt)
        curses.echo()
        result = stdscr.getstr(row, len(prompt)).decode('utf-8')
        curses.noecho()
        return result

    def input_students(self, stdscr):
        stdscr.clear()
        n = int(self.get_input(stdscr, "Enter the number of students: ", 0))
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Inputting Student {i+1}/{n} ---", curses.A_BOLD)
            sid = self.get_input(stdscr, "Student ID: ", 2)
            name = self.get_input(stdscr, "Name: ", 3)
            dob = self.get_input(stdscr, "DoB: ", 4)
            self.students.append(Student(sid, name, dob))
            
        stdscr.clear()
        stdscr.addstr(2, 0, "Students added! Press any key...", curses.A_BOLD)
        stdscr.getch()

    def input_courses(self, stdscr):
        stdscr.clear()
        n = int(self.get_input(stdscr, "Enter the number of courses: ", 0))
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Inputting Course {i+1}/{n} ---", curses.A_BOLD)
            cid = self.get_input(stdscr, "Course ID: ", 2)
            name = self.get_input(stdscr, "Name: ", 3)
            credits = int(self.get_input(stdscr, "Credits: ", 4))
            self.courses.append(Course(cid, name, credits))
            
        stdscr.clear()
        stdscr.addstr(2, 0, "Courses added! Press any key...", curses.A_BOLD)
        stdscr.getch()

    def input_marks(self, stdscr):
        stdscr.clear()
        cid = self.get_input(stdscr, "Enter Course ID to input marks: ", 0)
        
        if not any(c.get_id() == cid for c in self.courses):
            stdscr.addstr(2, 0, "Course not found! Press any key...")
            stdscr.getch()
            return

        for i, student in enumerate(self.students):
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Inputting Marks for Course: {cid} ---", curses.A_BOLD)
            mark_str = self.get_input(stdscr, f"[{i+1}/{len(self.students)}] Enter mark for {student.get_name()}: ", 2)
            student.add_mark(cid, float(mark_str))
            
        stdscr.clear()
        stdscr.addstr(2, 0, "Marks saved! Press any key...", curses.A_BOLD)
        stdscr.getch()

    def show_gpa_list(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, f"{'ID':<10} | {'Name':<20} | {'GPA':<5}", curses.A_REVERSE)
        
        for s in self.students:
            s.calculate_gpa(self.courses)
            
        sorted_students = sorted(self.students, key=lambda s: s.get_gpa(), reverse=True)
        
        row = 2
        for s in sorted_students:
            stdscr.addstr(row, 0, f"{s.get_id():<10} | {s.get_name():<20} | {s.get_gpa():.1f}")
            row += 1
            
        stdscr.addstr(row + 2, 0, "Press any key to return to menu...")
        stdscr.getch()

    def run(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "=== HOÀNG BẢO ANH - STUDENT MANAGEMENT ===", curses.A_BOLD)
            stdscr.addstr(2, 0, "1. Input Students")
            stdscr.addstr(3, 0, "2. Input Courses")
            stdscr.addstr(4, 0, "3. Input Marks")
            stdscr.addstr(5, 0, "4. Show Sorted GPA List")
            stdscr.addstr(6, 0, "0. Exit")
            
            choice = self.get_input(stdscr, "Your choice: ", 8)
            
            if choice == '1':
                self.input_students(stdscr)
            elif choice == '2':
                self.input_courses(stdscr)
            elif choice == '3':
                self.input_marks(stdscr)
            elif choice == '4':
                self.show_gpa_list(stdscr)
            elif choice == '0':
                break

if __name__ == "__main__":
    sys = ManagementSystem()
    curses.wrapper(sys.run)