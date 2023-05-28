# height = 50
# temperature = 60
# def add_value(a,b):
#     return a + b
#     # print (sum)
# print(add_value(height,temperature))
#

'''
PEP-8 Conventions for prototyping a class

    Class names should be written in UpperCamelCase.
    Class attributes and methods should be written in snake_case.
    We should separate classes with 2 blank lines and methods with a blank line.
    objects or instances are defined with snake_case representation as in variables.

'''
# class Person :
#     first_name = 'siraj'
#     last_name = 'khan'
#
#     def show_full_name(self):
#         print (f'full name is {self.first_name}{self.last_name}')
#
# a = Person()
# a.show_full_name()
#





'''class Person:
    first_name = 'Suraj'
    last_name = 'Rajbanshi'
    address = 'Biratnagar'
    phone_number = '98*********'
    def show_details(self):
        return f'My name is {self.first_name} {self.last_name}'
    def details(self):
        return f'Full Name: {self.first_name} {self.last_name}, Address: {self.address}, Phone Number:{self.phone_number}'
a = Person()
print(a.show_details())
print(a.details())
'''
'''Attributes, Methods, and the self parameter'''
''' 
    All the variables defined inside a class are attributes.
    Attribute acts as a state of the class which changes over time and condition
    All functions defined inside a class are known as methods
    All instance methods use the first parameter self which references the instance itself.
    the __init__() method do not need to be called and gets automatically called once the object gets initialized.
'''
# class person:
#     species = 'Human'
#
#
#     def __init__(self, first_name, last_name):
#         print(f'{self.species} ')
#         self.first_name = first_name
#         self.last_name = last_name
#     def full_name (self):
#         print(f'Full Name: {self.first_name} {self.last_name}')
# a = person( 'Suraj', 'Rajbanshi')
# (a.full_name())
#
#
# Person = person('John','Snow')
# print(Person.first_name)
# print(Person.last_name)
# (Person.full_name())


#
# class it:
#     department = 'Backend'
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def employee_details(self):
#         print(f'Employee First Name is {self.first_name} and Last Name is {self.last_name} and is from department {self.department}')
# IT = it('abc','xyz')
# IT.employee_details()
#

# class Animal:
#     category = 'Vertebrate'
#     legs = 4
#     def __init__(self,name,child):
#         self.name = name
#         self.child = child
#         word = 'Moo'
# print(Animal.category)
# animal = Animal('cow','5')
# print(animal.name,animal.child)



# class Person:
#     '''
#     Hello World
#     '''
#
#
#
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def __str__(self):
#         return f'Person<{self.first_name}>'
# john = Person('John','Lennon',50)
# print('The String Representation is:',john.__str__())
# print('The Dictionary Representation is :',john.__dict__)
# print('The Documentary Representation is :', john.__doc__)
# print('The Size of Class is ' ,john.__sizeof__())



# x = 5
# y = 10.5
# z = True
# a = 'Hello World'
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))

class animal:
    def __init__(self,name,word):
        self.name = name
        self.word = word
    def speak(self):
        print(f'name of cow is {self.name} and speaks {self.word}')
cow = animal(name= input('name of cow'),word ='HAIYA HAIYA')
(cow.speak())

print(cow.__doc__)
print(cow.__sizeof__())
print(cow.__dict__)


