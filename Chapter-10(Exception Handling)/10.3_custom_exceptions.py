# class AgeError(Exception):
#     min_age = 0
#     max_age = 100
#
#     def __init__(self,age,*args):
#         super().__init__(*args)
#         self.age = age
#
#     def __str__(self):
#         return f'The age {self.age} is not in between {self.min_age} and {self.max_age}'




class Length_Error(Exception):
    def __init__(self,value:int,*args:object):
        self.value = value
    def __str__(self):
        return f'The length {self.value} is not not possible'

class length:
    def __init__(self,value):
        if value < 0:
            raise Length_Error(value)
        self.value = value

l1 = length(10)
l2 = length(-5)




