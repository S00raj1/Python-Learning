class Parent1:

    x = 5
class Parent2:
    x = 10

class Child(Parent2,Parent1):
    pass


c1 = Child()
print(c1.x)

class Shop:
    def __init__(self) ->None:
        self.__reg_no = 0

    def get_reg_no(self):
        return self.__reg_no
    def set_reg_no(self,value):
        self.__reg_no = value

class CoffeeShop(Shop):
    coffee_price = 30

class Bakery(Shop):
    dough_nut_price = 10

class Resturant(CoffeeShop,Bakery):
    pizza_price = 20

    def __init__(self,reg_no) ->None:
        super().__init__()
        self.set_reg_no(reg_no)
r1 = Resturant('CagtuCafe')
r1.coffee_price = 15
print(r1.get_reg_no())
print(r1.dough_nut_price)
print(r1.pizza_price)
print(r1.coffee_price)



print(isinstance(r1,Resturant))
print(isinstance(r1,Bakery))
print(isinstance(r1,CoffeeShop))
print(isinstance(r1,Shop))
print(issubclass(Resturant,Shop))