# from typing import List
# MALE = 'male'
# FEMALE = 'female'
#
# class Students:
#     def __init__(self,name,roll,gender):
#         self.name = name
#         self.roll = roll
#         self.gender = gender
#
#     def __str__(self) -> str:
#         return self.name
#     def __repr__(self)-> None:
#         return self.__str__()
#
# class ClassRoom:
#     def __init__(self,name):
#         self.name = name
#         self.students : list[Students] = []
#
#     def __add__(self, other:'ClassRoom'):
#         result = ClassRoom(f'{self.name}_{other.name}')
#         result.students = [*self.students, *other.students]
#         return result
#
# py_class = ClassRoom('Python')
# py_class.students.append(Students('John',1,'Male'))
# py_class.students.append(Students('Jonu',2,'Male'))
# java_class = ClassRoom('Java')
# java_class.students.append(Students('Sonu',3,'Male'))
# java_class.students.append(Students('Soni',4,'Female'))
#
# merged = py_class + java_class
# print(merged.students)
# print(merged.name)