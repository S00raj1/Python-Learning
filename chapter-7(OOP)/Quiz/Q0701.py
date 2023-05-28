
"""

Create a python class with following properties:
1. private class attribute
2. public class attribute
3. instance attribute
4. initializer method
5. string representation method [__str__()]
"""

class Cagtu:
    __name = 'Unknown'
    age = 20
    def __init__(self,name):
        self.name = name

    def __str__(self,name) ->str:
        return self.name

a = Cagtu('xyz')
print(a.name)