from TooManyStudentsException import TooManyStudentsException


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.__max_students = 10

    def add_student(self, student):
        if len(self.group) >= self.__max_students:
            raise TooManyStudentsException("Too many students: ", self.__max_students)

        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student)
        return f'Number:{self.number}\n {all_students} '