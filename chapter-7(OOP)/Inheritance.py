
"""
# Inheritance
- This concept is exactly similar to biological inheritance where child inherits the feature of parent.
- in inheritance, there exists a parent class and child classes which inherits parent's behaviors.
- The base class will be the parent class and the class that is derived from the base class will
  be treated as a child class.
Basic Structure
class Parent:
    <attributes>
    <methods>
class Child(Parent):
    <attributes>
    <methods>
"""



class Rectangle:
    def __init__(self,width:float,height:float):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2*(self.width+self.height)
    def area(self):
        return self.width*self.height
    def diagonal_length(self):
        return (self.width**2 + self.height**2)/(1/2)

class Square(Rectangle):
    def __init__(self,width):
        super().__init__(width=width,height=width)
    def diagonal_length(self):
        return self.width * (2**.5)

room_1 = Rectangle(10,20)
print(room_1.area())
print(room_1.perimeter())
print(room_1.diagonal_length())

room_2 = Square(5)
print(f'the area of square is  {room_2.area()}')
print(f'the perimeter of square is  {room_2.perimeter()}')





# class Parent:
#     def __init__(self,hair,caste,color):
#         self.hair = hair
#         self.caste = caste
#         self.color = color
#
#     def Hair_color(self):
#         return self.color
#         print(f'The Color of hair is {self.hair}')
#
#     def Caste(self):
#         return self.caste
#         print(f'The caste is {self.caste}')
#
#     def Color(self):
#         return self.caste
#         print(f'The skin color is {self.color}')
#
# class Child(Parent):
#     def __init__(self,hair,caste,color):
#         super().__init__(hair = hair,caste = caste, color = color)
#
#     def Hair_color(self):
#         return self.hair
#         print(f'The Color of hair is {self.hair}')
#
#
#     def Caste(self):
#         return self.caste
#         print(f'The caste is {self.caste}')
#
#     def Color(self):
#         return self.color
#         print(f'The skin color is {self.color}')
#
# first = Parent(hair='black',caste = 'cagtu', color= 'cream')
# second = Child(hair=first.hair,caste=first.caste,color=first.color)
# # print(first.color)
# print(second.Hair_color())
# print(second.Caste())
# print(second.Color())





class Parent:
    pass
class Child(Parent):
    pass

obj1 = Parent()
obj2 = Child()
print(isinstance(room_2,Square))
print(isinstance(room_1,Rectangle))
print(isinstance(room_1,Square))
print(isinstance(room_2,Rectangle))

print(issubclass(Square,Square))
print(issubclass(Rectangle,Rectangle))
print(issubclass(Rectangle,object))