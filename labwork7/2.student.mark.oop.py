class Person:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._dob = ""

    def input(self):
        self._id = input("ID: ")
        self._name = input("Full Name: ")
        self._dob = input("Date of Birth (DoB): ")

    def list(self):
        print("ID: {:<10} | Name: {:<15} | DoB: {}".format(self._id, self._name, self._dob))

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob


class Student(Person):
    def __init__(self):
        super().__init__()
        self.__marks = {}

    def input(self):
        self._id = input("Student ID: ")
        self._name = input("Full Name: ")
        self._dob = input("Date of Birth (DoB): ")

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_mark(self, course_id):
        return self.__marks.get(course_id, "N/A")


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")

    def list(self):
        print("ID: {:<10} | Name: {}".format(self.__id, self.__name))

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_students(self):
        print("\n")
        n = int(input("Enter the number of students: "))
        for i in range(n):
            print("\n--- Student {} Information ---".format(i + 1))
            student = Student()
            student.input()
            self.__students.append(student)

    def input_courses(self):
        print("\n")
        n = int(input("Enter the number of courses: "))
        for i in range(n):
            print("\n--- Course {} Information ---".format(i + 1))
            course = Course()
            course.input()
            self.__courses.append(course)

    def list_students(self):
        print("\n\n--- LIST OF STUDENTS ---")
        for student in self.__students:
            student.list()

    def list_courses(self):
        print("\n--- LIST OF COURSES ---")
        for course in self.__courses:
            course.list()

    def input_marks(self):
        print("\n\n==========================================")
        print("               INPUT MARKS                ")
        print("==========================================\n")

        c_id = input("Enter Course ID to input marks: ")

        course_exists = False
        for course in self.__courses:
            if course.get_id() == c_id:
                course_exists = True
                break

        if not course_exists:
            print("\n-> ERROR: Course ID does not exist! Please try again.\n")
            return

        print("\n--- Entering marks for Course ID: {} ---".format(c_id))
        for student in self.__students:
            mark = float(input("Enter mark for {} (ID: {}): ".format(student.get_name(), student.get_id())))
            student.add_mark(c_id, mark)
        print("\n-> Marks saved successfully!")

    def show_marks(self):
        print("\n\n==========================================")
        print("               SHOW MARKS                 ")
        print("==========================================\n")

        show_id = input("Enter Course ID to show marks: ")

        course_name = ""
        for course in self.__courses:
            if course.get_id() == show_id:
                course_name = course.get_name()
                break

        if course_name == "":
            print("\n-> ERROR: No marks found for this Course ID!\n")
            return

        print("\n--- MARKS FOR COURSE: {} (ID: {}) ---".format(course_name.upper(), show_id))
        for student in self.__students:
            mark = student.get_mark(show_id)
            print("ID: {:<10} | Name: {:<15} | Mark: {}".format(student.get_id(), student.get_name(), mark))
        print("\n")

    def run(self):
        self.input_students()
        self.input_courses()
        self.list_students()
        self.list_courses()

        while True:
            print("\n\n==========================================")
            print("                 MAIN MENU                ")
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