'''

# Class Methods and static methods
Class Methods
- Class methods are special kind of methods that are bound to the class instead of the instance
- If we create an instance and change the property of the object, it is not going to affect the property
  of the classmethod.
Static Methods
- Static methods are methods that do not bind to anything at all and simply return the underlying function
  without any transformation.
- They just behave like a function. Only the difference is they are called along with the class name.
'''

# class Animal:
#     legs = 4
#     @classmethod
#     def print_legs(cls):
#         print('Total no. of legs : ', cls.legs)
#
#     def print_legs_1(self):
#         print('Total no. of legs:', self.legs)
#
# print(Animal.legs)
# Animal.print_legs()
# Animal().print_legs()
#
# human = Animal()
# human.legs = 2
# human.print_legs()
#
# print(human.legs)
# print(Animal.legs)



# class length:
#     cm = 5438
#     @staticmethod
#     def cm_to_m(value:float):
#         return value/100
#
#     @staticmethod
#     def m_to_cm(value:float):
#         return value*100
#
# class weight:
#     @staticmethod
#     def kg_to_lb(value:float):
#         return value*2.20462
#
#     @staticmethod
#     def lb_to_kg(value:float):
#         return value/ 2.20462
#
# print(length.cm_to_m(length.cm))
# print(length.m_to_cm(length.cm))
# print(weight.kg_to_lb(length.cm))
# print(weight.lb_to_kg(length.cm))


