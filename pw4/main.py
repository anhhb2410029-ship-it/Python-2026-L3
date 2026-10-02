import curses
from input import get_input, input_students, input_courses, input_marks
from output import show_gpa_list

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def run(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "=== HOÀNG BẢO ANH - STUDENT MANAGEMENT ===", curses.A_BOLD)
            stdscr.addstr(2, 0, "1. Input Students")
            stdscr.addstr(3, 0, "2. Input Courses")
            stdscr.addstr(4, 0, "3. Input Marks")
            stdscr.addstr(5, 0, "4. Show Sorted GPA List")
            stdscr.addstr(6, 0, "0. Exit")
            
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
                break

if __name__ == "__main__":
    sys = ManagementSystem()
    curses.wrapper(sys.run)