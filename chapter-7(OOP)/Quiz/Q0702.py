'''Create a class named Person and add the following attributes and methods:
    - name:     Instance attribute
    - age:      Instance attribute
    - gender:   Instance attribute
    - weight:   Class attribute
    - year_of_birth():
        Returns the year by subtracting the age from the current year.
    - get_pronouns():
        Returns list of ['he', 'his', 'him'] or ['she', 'her', 'hers'] by checking the gender
    the initializer method should take name, age, and gender
'''

import datetime
class Person:
    weight = 50
    s=['she','her']
    m = ['he', 'his', 'him']
    def __init__(self,name,age,gender=True):
        self.name = name
        self.age = age
        self.gender = gender

    def year_of_birth(self,age):
        current_year = datetime.date.today().year
        year = current_year - age
        return f'{self.name} was born in', year

    def get_pronouns(self):
        super().__init__()

        if self.gender==True:
            print(Person.m)
        else:
            print(Person.s)



per = Person(name = input('Name'),age =int(input('Enter age')),gender =bool(input('Enter your gender True if male or False if Female')))
print(*per.year_of_birth(age = per.age))
per.get_pronouns()
