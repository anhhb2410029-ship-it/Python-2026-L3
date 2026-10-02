import curses

def show_gpa_list(stdscr, students_list, courses_list):
    stdscr.clear()
    stdscr.addstr(0, 0, f"{'ID':<10} | {'Name':<20} | {'GPA':<5}", curses.A_REVERSE)
    
    for s in students_list:
        s.calculate_gpa(courses_list)
        
    sorted_students = sorted(students_list, key=lambda s: s.get_gpa(), reverse=True)
    
    row = 2
    for s in sorted_students:
        stdscr.addstr(row, 0, f"{s.get_id():<10} | {s.get_name():<20} | {s.get_gpa():.1f}")
        row += 1
        
    stdscr.addstr(row + 2, 0, "Press any key to return to menu...")
    stdscr.getch()