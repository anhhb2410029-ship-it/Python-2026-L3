import curses
import os
import zipfile
import pickle
import csv
import pandas as pd
from input import get_input, input_students, input_courses, input_marks
from output import show_gpa_list

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.load_data()

    def load_data(self):
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as zf:
                zf.extract("data.pkl")
            
            if os.path.exists("data.pkl"):
                with open("data.pkl", "rb") as f:
                    data = pickle.load(f)
                    self.students = data.get('students', [])
                    self.courses = data.get('courses', [])
                os.remove("data.pkl")

    def compress_data(self):
        with open("data.pkl", "wb") as f:
            pickle.dump({'students': self.students, 'courses': self.courses}, f)
            
        with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write("data.pkl")
        
        if os.path.exists("data.pkl"):
            os.remove("data.pkl")

    def export_csv(self):
        with open("students.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "dob"])
            for s in self.students:
                writer.writerow([s.get_id(), s.get_name(), s._dob])

        with open("courses.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "credits"])
            for c in self.courses:
                writer.writerow([c.get_id(), c._name, c.get_credits()])

        with open("marks.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["student_id", "course_id", "mark"])
            for s in self.students:
                for cid, mark in s._Student__marks.items():
                    writer.writerow([s.get_id(), cid, mark])

    def query_pandas(self, stdscr):
        self.export_csv()
        stdscr.clear()
        
        try:
            df = pd.read_csv("students.csv")
            query_str = get_input(stdscr, "Enter Pandas query (e.g., name == 'HOÀNG BẢO ANH'): ", 0)
            
            result = df.query(query_str)
            
            stdscr.clear()
            stdscr.addstr(0, 0, "=== QUERY RESULTS ===", curses.A_BOLD)
            
            if result.empty:
                stdscr.addstr(2, 0, "No records found.")
            else:
                lines = result.to_string().split('\n')
                for idx, line in enumerate(lines):
                    stdscr.addstr(2 + idx, 0, line)
                    
            stdscr.addstr(len(result) + 4, 0, "Press any key to return...")
            
        except Exception as e:
            stdscr.clear()
            stdscr.addstr(0, 0, f"Error: {str(e)}")
            stdscr.addstr(2, 0, "Press any key to return...")
            
        stdscr.getch()

    def run(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "=== HOÀNG BẢO ANH - STUDENT MANAGEMENT (PW6 - PICKLE & PANDAS) ===", curses.A_BOLD)
            stdscr.addstr(2, 0, "1. Input Students")
            stdscr.addstr(3, 0, "2. Input Courses")
            stdscr.addstr(4, 0, "3. Input Marks")
            stdscr.addstr(5, 0, "4. Show Sorted GPA List")
            stdscr.addstr(6, 0, "5. Pandas Query (EXTRA)")
            stdscr.addstr(7, 0, "0. Exit (Save and Compress)")
            
            choice = get_input(stdscr, "Your choice: ", 9)
            
            if choice == '1':
                input_students(stdscr, self.students)
            elif choice == '2':
                input_courses(stdscr, self.courses)
            elif choice == '3':
                input_marks(stdscr, self.students, self.courses)
            elif choice == '4':
                show_gpa_list(stdscr, self.students, self.courses)
            elif choice == '5':
                self.query_pandas(stdscr)
            elif choice == '0':
                self.export_csv()
                self.compress_data()
                break

if __name__ == "__main__":
    sys = ManagementSystem()
    curses.wrapper(sys.run)