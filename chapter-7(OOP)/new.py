class Student:
    def __init__(self, name):
        self.name = name

Student.grade = 1  # Monkey Patching Class attribute
Student.major = 'science'
john = Student("John Doe")

print(john.name)
john.roll = 5  # Monkey Patching instance attribute
print(john.roll)


def display_name(self):
    print(self.name)


def display_major(self):
    print(self.major)


Student.display_name = display_name  # Monkey patching class attribute
Student.display_major = display_major

john.display_name()


jane = Student("Jane")
print(jane.roll)