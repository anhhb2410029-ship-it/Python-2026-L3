
class Person:
    def __init__(self):
        
        self._id = ""
        self._name = ""
        self._dob = ""

    
    def input_info(self):
        self._id = input("ID: ")
        self._name = input("Name: ")
        self._dob = input("Date of Birth: ")

    def list_info(self):
        print(f"ID: {self._id:<10} | Name: {self._name:<15} | DoB: {self._dob}")

class Student(Person):
    def __init__(self):
        super().__init__()
        self.__marks = {}  

    
    def input_info(self):
        print("--- Enter Student Information ---")
        super().input_info()

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_mark(self, course_id):
        return self.__marks.get(course_id, "N/A")
    
    def get_id(self):
        return self._id

class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

   
    def input_info(self):
        print("--- Enter Course Information ---")
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")

    def list_info(self):
        print(f"ID: {self.__id:<10} | Name: {self.__name}")
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name

class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_students(self):
        n = int(input("\nEnter the number of students: "))
        for _ in range(n):
            student = Student()
            student.input_info() 
            self.__students.append(student)

    def input_courses(self):
        n = int(input("\nEnter the number of courses: "))
        for _ in range(n):
            course = Course()
            course.input_info()
            self.__courses.append(course)

    def list_students(self):
        print("\n--- LIST OF STUDENTS ---")
        for student in self.__students:
            student.list_info()

    def list_courses(self):
        print("\n--- LIST OF COURSES ---")
        for course in self.__courses:
            course.list_info()

    def input_marks(self):
        c_id = input("\nEnter Course ID to input marks: ")
        
        # Kiểm tra Course ID
        if not any(c.get_id() == c_id for c in self.__courses):
            print("\n-> ERROR: Course ID does not exist! Please try again.\n")
            return

        print(f"\n--- Entering marks for Course ID: {c_id} ---")
        for student in self.__students:
            mark = float(input(f"Enter mark for {student._name} (ID: {student.get_id()}): "))
            student.add_mark(c_id, mark)
        print("\n-> Marks saved successfully!")

    def show_marks(self):
        c_id = input("\nEnter Course ID to show marks: ")
        course_name = next((c.get_name() for c in self.__courses if c.get_id() == c_id), None)
        
        if not course_name:
            print("\n-> ERROR: No marks found for this Course ID!\n")
            return

        print(f"\n--- MARKS FOR COURSE: {course_name.upper()} (ID: {c_id}) ---")
        for student in self.__students:
            mark = student.get_mark(c_id)
            print(f"ID: {student.get_id():<10} | Name: {student._name:<15} | Mark: {mark}")

    def run(self):
        self.input_students()
        self.input_courses()
        self.list_students()
        self.list_courses()

        while True:
            print("\n\n==========================================")
            print("                MAIN MENU                 ")
            print("==========================================")
            print("1. Input marks for a course")
            print("2. Show marks for a course")
            print("0. Exit program")
            
            choice = input("Enter your choice (1/2/0): ")
            
            if choice == '1':
                self.input_marks()
            elif choice == '2':
                self.show_marks()
            elif choice == '0':
                print("\nExiting... Goodbye!\n")
                break
            else:
                print("\n-> ERROR: Invalid choice! Please enter 1, 2, or 0.")

if __name__ == "__main__":
    system = ManagementSystem()
    system.run()