class TooManyStudentsException(Exception):

    def __init__(self, message, x):
        super().__init__()
        self.message = message
        self.x = x

    def get_exception_message(self):
        return self.message