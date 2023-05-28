# class ClassRoom:
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#
#     def add_students(self,*students):
#         self.students.extend(students)
#
#     def __add__(self, other):
#         new_Classroom = ClassRoom(f'{self.name} ,{other.name}')
#         new_Classroom.students = [*self.students, *other.students]
#         return new_Classroom
# c1 = ClassRoom('Python')
# c1.add_students('Suraj','Himal','Saiman')
#
# c2 = ClassRoom('UI/UX')
# c2.add_students('Shardul','Shashank')
#
# c3 = ClassRoom('QA')
# c3.add_students('Soyuj','Dipesh')
#
# c4 = c1 + c2 + c3
# print(c4.name)
# print(c4.students)


class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_students(self,*students):
        self.students.extend(students)

    def __add__(self, other):
        new_classroom = ClassRoom(f'{self.name} and {other.name}')
        new_classroom.students = [*self.students, *other.students]
        return new_classroom

c1 = ClassRoom('Python')
c1.add_students('John','Jane')

c2 = ClassRoom('Java')
c2.add_students('Mark','Satoshi')

c3 = c1+c2
print(c3.name)
print(c3.students)