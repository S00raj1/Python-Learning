# class student:
#     def __init__(self,count:int):
#         self.__count = count
#
#     def get_count(self):
#         return self.__count
#
#     def set_count(self,value):
#         self.__count = value
#
# class_1 = student(10)
# print(class_1.get_count())
# class_1.set_count(12)
# print(class_1.get_count())

# class students:
#     def __init__(self,count:int):
#         self.__count = count
#
#     @property
#     def Count(self):
#         return self.__count
#     @Count.setter
#     def Count(self,value):
#         self.__count = value
#         print(f'The value of Count is changed to {self.__count}')
#
#     @Count.deleter
#     def Count(self):
#         self.__count = 0
#         print('The value of count is deleted')
#
# hello = students(10)
# print(hello.Count)
#
# del hello.Count
#













class Office:
    def __init__(self,workers:int):
        self.__workers = workers

    @property
    def office(self):
        return self.__workers

    @office.setter
    def office(self,value):
        self.__workers = value
        print(f'The no of workers in the office is {self.__workers}')

cagtu = Office(35)
print(cagtu.office)
cagtu.office = 40
# print(cagtu.office)

























