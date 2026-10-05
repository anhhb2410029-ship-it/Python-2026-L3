import curses
import os
import zipfile
from input import get_input, input_students, input_courses, input_marks
from output import show_gpa_list
from domains.student import Student
from domains.course import Course

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.load_data()

    def load_data(self):
       
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as zf:
                zf.extractall()
            
            if os.path.exists("students.txt"):
                with open("students.txt", "r") as f:
                    for line in f:
                        sid, name, dob = line.strip().split(',')
                        self.students.append(Student(sid, name, dob))
                        
            if os.path.exists("courses.txt"):
                with open("courses.txt", "r") as f:
                    for line in f:
                        cid, name, credits = line.strip().split(',')
                        self.courses.append(Course(cid, name, int(credits)))
                        
            if os.path.exists("marks.txt"):
                with open("marks.txt", "r") as f:
                    for line in f:
                        sid, cid, mark = line.strip().split(',')
                        student = next((s for s in self.students if s.get_id() == sid), None)
                        if student:
                            student.add_mark(cid, float(mark))

    def compress_data(self):
        
        files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
        with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zf:
            for file in files_to_compress:
                if os.path.exists(file):
                    zf.write(file)
                    os.remove(file) 

    def run(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "=== HOÀNG BẢO ANH - STUDENT MANAGEMENT ===", curses.A_BOLD)
            stdscr.addstr(2, 0, "1. Input Students")
            stdscr.addstr(3, 0, "2. Input Courses")
            stdscr.addstr(4, 0, "3. Input Marks")
            stdscr.addstr(5, 0, "4. Show Sorted GPA List")
            stdscr.addstr(6, 0, "0. Exit (Save and Compress)")
            
            choice = get_input(stdscr, "Your choice: ", 8)
            
            if choice == '1':
                input_students(stdscr, self.students)
            elif choice == '2':
                input_courses(stdscr, self.courses)
            elif choice == '3':
                input_marks(stdscr, self.students, self.courses)
            elif choice == '4':
                show_gpa_list(stdscr, self.students, self.courses)
            elif choice == '0':
                self.compress_data()
                break

if __name__ == "__main__":
    sys = ManagementSystem()
    curses.wrapper(sys.run)