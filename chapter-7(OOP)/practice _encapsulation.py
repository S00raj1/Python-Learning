# class Student:
#
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#
#     def __str__(self) -> str:
#         return self.name
#
#
# class ClassRoom:
#     def __init__(self, name):
#         self.__is_large = False
#         self.__students = []
#         self.name = name
#
#     def add_student(self, student: Student):  # setter
#         self.__students.append(student)
#         self.__is_large = True if self.__students.__len__() > 3 else False
#
#     def remove_student(self, student: Student):  # setter / deleter
#         if student in self.__students:
#             self.__students.remove(student)
#             self.__is_large = True if self.__students.__len__() > 3 else False
#         else:
#             print(f"Student with name {student.name} does not exist")
#
# john = Student("Jon Doe", 1)
# py_class = ClassRoom("Python for Beginners")
# py_class.add_student(john)
# py_class.add_student(Student("John Lennon", 2))
# py_class.add_student(Student("John Legend", 3))
# py_class.add_student(Student("John Denver", 4))
# # here the value __is_large will be set to True
#
# py_class.remove_student(john)
# # here the value __is_large will be set to False


# class MyClass:
#     __value = 1
#     def get_value(self):
#         return self.__value
#
#     def set_value(self,value):
#         self.__value = value
#
# cls1 = MyClass()
# cls1.set_value(5)
# print(cls1.get_value())



MALE = 'male'
FEMALE = 'female'

class Student:
    def __init__(self,name,roll,gender):
        self.name = name
        self.roll = roll
        self.gender = gender

    def __str__(self) ->str:
        return f'{self.roll}\t{self.name}'

class ClassRoom:
    def __init__(self,name,class_teacher):
        self.__is_large = False
        self.__students = []
        self.name = name
        self.class_teacher = class_teacher

    def add_student(self,student:Student):
        # print('[Adding Student ]'.center(80,'='))
        self.__students.append(student)
        if self.__students.__len__() > 3:
            self.__is_large = True

        else:
            self.__is_large = False

    def remove_students(self,student:Student):
        # print('[Removing Students]'.center(80,'='))
        if student in self.__students:
            print('[Removing Students]'.center(80, '='))
            print(f'{student.name} is removed')
            self.__students.remove(student)
            if self.__students.__len__() > 3:
                self.__is_large = True
            else:
                self.__is_large = False
        else:
            print(f'Student with name {student.name} does not exist')

    def describe(self):
        print('students')
        for student in self.__students:
            print(student)
        print('large:', self.__is_large)

py_class = ClassRoom('Python for Beginners','Sudip Ghimire')
name1= Student('Jon Doe',1,MALE)
name2=Student('Suraj',2,MALE)
name3=Student('Saiman hutiya',4,MALE)
py_class.add_student(name3)
py_class.remove_students(name3)


# py_class.add_student(jon)
# py_class.add_student(Student('Jane Doe',2,FEMALE))
#
#
#
# py_class.remove_students(Student(jon,1,MALE))
# py_class.remove_students(Student('jane',2,FEMALE))
# py_class.describe()