from Human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__str__ == other.__str__
        return NotImplemented

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}\n"