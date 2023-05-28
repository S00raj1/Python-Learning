# class MyClass:
#     _name = 'Unknown'
#     __age = 20
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,age):
#         self.__age = age
#         self._name = f'Unknown: {age}'
# b= MyClass()
# print()
# b.set_age(30)
# print(b.get_age())
# print(b._name)


#
# class Myclass:
#     _name = 'Homaale'
#     __age = 1
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         self.__age = age
#         self._name = f'Homaale : {age}'
#
# b= Myclass()
# print()
# b.set_age(4)
# print(b.get_age())
# print(b._name)

# xample 2: An advanced class representation which takes list of Student objects and changes the state __is_large when the number of students is more than 3

# class Student:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll
#     def __str__(self) -> str:
#         return self.name
#
# class ClassRoom:
#     def __init__(self,name):
#         self.__is_large = False
#         self.__students =[]
#         self.name = name
#     def add_student(self,student:Student):
#         self.__students.append(student)
#         self.__is_large = True if self.__students.__len__() > 3 else False
#     def remove_student(self, student:Student):
#         if student in self.__students:
#             self.__students.remove(student)
#             self.__is_large = True if self.__students.__len__()>3 else False
#         else:
#             print(f'Student with name {student.name}does not exist')
# john = Student('John Doe',1)
# py_class = ClassRoom('Python for Beginners')
# py_class.add_student(john)
# py_class.add_student(Student('John Lennon', 2))
# py_class.add_student(Student('John Legend', 3))
# py_class.add_student(Student('John Denver', 4))
# py_class.add_student(Student('John Denver', 2))
#
#
# print()
#
#
# py_class.remove_student(john)



# class Student:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll
#
#     def __str__(self) ->str:
#         return self.name
#
# class ClassRoom:
#     def __init__(self,name):
#         self.__is_large = False
#         self.__students = []
#
#     def add_students(self, student: Student):
#         self.__students.append(student)
#         self.__is_large = True if self.__students.__len__() > 3 else False
#
#     def remove_students(self,student: Student):
#         if student in self.__students:
#             self.__students.remove(student)
#             self.__is_large = True if self.__students.__len__() >3 else False
#         else:
#             print(f'Student with name {student.name} does not exist')
#
# john = Student('john Doe ', 1)
# py_class = ClassRoom('Python for Beginners')
# py_class.add_students(john)
# py_class.add_students(Student('John Lennon', 2))
# py_class.add_students(Student('John Legend', 3))
# py_class.add_students(Student('John Abraham', 4))
#
# py_class.remove_students(john)
# py_class.remove_students(john)

# class Students:
#     def __init__(self,count:int):
#         self.__count = count
#
#     @property
#     def count(self):
#         return self.__count
#
#     @count.setter
#     def count(self,value):
#         print('i can do other things while updating my value')
#         self.__count = value
#
#     @count.deleter
#     def count(self):
#         self.__count = 0
#
# class_1 = Students(10)
# print(class_1.count)
#
# class_1.count = 11
# print(class_1.count)
#
#
# del class_1.count
# print(class_1.count)


# class College:
#     def __init__(self,students:int):
#         self.__students = students
#
#     @property
#     def students(self):
#         return self.__students
#     @students.setter
#     def students(self,value):
#         print('Hello world')
#         self.__students = value
#
#     @students.deleter
#     def students(self):
#         self.__students = 20
#
# class_1 = College(50)
# print(class_1.students)
# class_1.students = 12
# print(class_1.students)
# del class_1.students
# print(class_1.students)



# class College:
#     def __init__(self,count):
#         self.__count = count
#
#     @property
#     def count(self):
#         return self.__count
#
#     @count.setter
#     def count(self,value):
#         print('The value of count  changes here after it is called')
#         self.__count = value
#
#     @count.deleter
#     def count(self):
#         print('the value of count is deleted after it is called')
#         self.__count = 0
#
# count_1 = College(20)
# print(count_1.count)
#
# count_1.count = 25
# print(count_1.count)
# del count_1.count
# print(count_1.count)
#
#
#
#



class cagtu:
    def __init__(self, count):
        self.__count = count
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self,value):
        print('it is the place where we can set the value of count')
        self.__count = value

    @count.deleter
    def count(self):
        self.__count = 0
count_1 = cagtu(15)
print(count_1.count)
count_1.count = 20
print(count_1.count)
del count_1.count
print(count_1.count)