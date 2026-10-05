
def input_students():
    students = []
    print("\n")
    n = int(input("Enter the number of students: "))
    
    for i in range(n):
        print("\n--- Student {} Information ---".format(i + 1))
        s_id = input("Student ID: ") 
        name = input("Full Name: ")
        dob = input("Date of Birth (DoB): ")
        students.append((s_id, name, dob))
        
    return students

def input_courses():
    courses = []
    print("\n")
    n = int(input("Enter the number of courses: "))
    
    for i in range(n):
        print("\n--- Course {} Information ---".format(i + 1))
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        courses.append((c_id, name))
        
    return courses

def input_marks(students, courses, marks):
    print("\n\n==========================================")
    print("               INPUT MARKS                ")
    print("==========================================\n")
    
    c_id = input("Enter Course ID to input marks: ")
    
    course_exists = False
    for course in courses:
        if course[0] == c_id:
            course_exists = True
            break
            
    if not course_exists:
        print("\n-> ERROR: Course ID does not exist! Please try again.\n")
        return 
        
    if c_id not in marks:
        marks[c_id] = {} 
        
    print("\n--- Entering marks for Course ID: {} ---".format(c_id))
    for student in students:
        mark = float(input("Enter mark for {} (ID: {}): ".format(student[1], student[0])))
        marks[c_id][student[0]] = mark 
    print("\n-> Marks saved successfully!")



def list_students(students):
    print("\n\n--- LIST OF STUDENTS ---")
    for student in students:
        
        print("ID: {:<10} | Name: {:<15} | DoB: {}".format(student[0], student[1], student[2]))

def list_courses(courses):
    print("\n--- LIST OF COURSES ---")
    for course in courses:
        print("ID: {:<10} | Name: {}".format(course[0], course[1]))

def show_marks(students, courses, marks):
    print("\n\n==========================================")
    print("               SHOW MARKS                 ")
    print("==========================================\n")
    
    show_id = input("Enter Course ID to show marks: ")
    
    if show_id not in marks:
        print("\n-> ERROR: No marks found for this Course ID!\n")
        return 
        
    course_name = ""
    for course in courses:
        if course[0] == show_id:
            course_name = course[1]
            break
            
    print("\n--- MARKS FOR COURSE: {} (ID: {}) ---".format(course_name.upper(), show_id))
    for student in students:
        student_id = student[0]
        if student_id in marks[show_id]:
           
            print("ID: {:<10} | Name: {:<15} | Mark: {}".format(student_id, student[1], marks[show_id][student_id]))
        else:
            print("ID: {:<10} | Name: {:<15} | Mark: N/A".format(student_id, student[1]))
    print("\n")



student_list = input_students()
course_list = input_courses()
marks_data = {} 

list_students(student_list)
list_courses(course_list)


while True:
    print("\n\n==========================================")
    print("                 MAIN MENU                ")
    print("==========================================")
    print("1. Input marks for a course")
    print("2. Show marks for a course")
    print("0. Exit program")
    
    choice = input("Enter your choice (1/2/0): ")
    
    if choice == '1':
        input_marks(student_list, course_list, marks_data)
    elif choice == '2':
        show_marks(student_list, course_list, marks_data)
    elif choice == '0':
        print("\nExiting... Goodbye!\n")
        break
    else:
        print("\n-> ERROR: Invalid choice! Please enter 1, 2, or 0.")