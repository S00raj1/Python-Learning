"""Monkey Patching
- it is the process of adding new variable or method to a class after it's been defined
- we can introduce a new instance attribute to an object even after it has been initialized
- monkey patching is useful when we do not want to perform inheritance or create a child class and
  change the behavior of the previously defined classes or previously instantianted objects.
- if we monkey patch the instance attribute, it is not going to change the class template, instead
  it affects only the instance we've created
"""


class Students:
    def __init__(self,name):
        self.name = name


Students.grade = 1
Students.major = 'science'
john = Students('John Doe')

print(john.name)
john.roll = 5
print(john.roll)

def display_name(self):
    print(self.name)


def display_major(self):
    print(self.major)


Students.display_name = display_name
Students.display_major = display_major

john.display_name()

jane = Students("Jane")
# jane.roll = 15
print(jane.major)