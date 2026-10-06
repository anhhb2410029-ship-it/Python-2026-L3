import curses
from domains.student import Student
from domains.course import Course

def get_input(stdscr, prompt, row):
    stdscr.addstr(row, 0, prompt)
    curses.echo()
    result = stdscr.getstr(row, len(prompt)).decode('utf-8')
    curses.noecho()
    return result

def input_students(stdscr, students_list):
    stdscr.clear()
    n = int(get_input(stdscr, "Enter the number of students: ", 0))
    for i in range(n):
        stdscr.clear()
        stdscr.addstr(0, 0, f"--- Inputting Student {i+1}/{n} ---", curses.A_BOLD)
        sid = get_input(stdscr, "Student ID: ", 2)
        name = get_input(stdscr, "Name: ", 3)
        dob = get_input(stdscr, "DoB: ", 4)
        students_list.append(Student(sid, name, dob))
            
    stdscr.clear()
    stdscr.addstr(2, 0, "Students added! Press any key...", curses.A_BOLD)
    stdscr.getch()

def input_courses(stdscr, courses_list):
    stdscr.clear()
    n = int(get_input(stdscr, "Enter the number of courses: ", 0))
    for i in range(n):
        stdscr.clear()
        stdscr.addstr(0, 0, f"--- Inputting Course {i+1}/{n} ---", curses.A_BOLD)
        cid = get_input(stdscr, "Course ID: ", 2)
        name = get_input(stdscr, "Name: ", 3)
        credits = int(get_input(stdscr, "Credits: ", 4))
        courses_list.append(Course(cid, name, credits))
            
    stdscr.clear()
    stdscr.addstr(2, 0, "Courses added! Press any key...", curses.A_BOLD)
    stdscr.getch()

def input_marks(stdscr, students_list, courses_list):
    stdscr.clear()
    cid = get_input(stdscr, "Enter Course ID to input marks: ", 0)
    
    if not any(c.get_id() == cid for c in courses_list):
        stdscr.addstr(2, 0, "Course not found! Press any key...")
        stdscr.getch()
        return

    for i, student in enumerate(students_list):
        stdscr.clear()
        stdscr.addstr(0, 0, f"--- Inputting Marks for Course: {cid} ---", curses.A_BOLD)
        mark_str = get_input(stdscr, f"[{i+1}/{len(students_list)}] Enter mark for {student.get_name()}: ", 2)
        student.add_mark(cid, float(mark_str))
            
    stdscr.clear()
    stdscr.addstr(2, 0, "Marks saved! Press any key...", curses.A_BOLD)
    stdscr.getch()