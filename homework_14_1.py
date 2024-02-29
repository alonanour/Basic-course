# Завдання 1 Виняток користувача
#
# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
# було порушено виняток користувача.
#
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}\n"


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


class TooManyStudentsException(Exception):

    def __init__(self, message, x):
        super().__init__()
        self.message = message
        self.x = x

    def get_exception_message(self):
        return self.message


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 23, 'Ann', 'Petrenko', 'AN146')
st4 = Student('Female', 32, 'Emma', 'Kim', 'AN147')
st5 = Student('Female', 19, 'Sofiia', 'Tkach', 'AN148')
st6 = Student('Female', 28, 'Alice', 'Koval', 'AN149')
st7 = Student('Female', 37, 'Mariia', 'Symonenko', 'AN150')
st8 = Student('Female', 21, 'Yana', 'Danylko', 'AN151')
st9 = Student('Male', 33, 'Max', 'Sivan', 'AN152')
st10 = Student('Female', 18, 'Marina', 'Shevchenko', 'AN153')
st11 = Student('Female', 29, 'Olha', 'Ivanenko', 'AN154')
gr = Group('PD1')


gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except TooManyStudentsException as err:
    print(err.get_exception_message())
    print(err.x)

print(f"\n{gr}")