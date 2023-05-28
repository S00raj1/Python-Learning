class Vehicle:
    wheels_count:int =4
    engine_type:str = 'Diesel Engine'
    braking_system:str = 'ABS'
    def __init__(self, name, brand):
        pass

class HeavyVehicle(Vehicle):
    max_load =4000
    mileage = 40
    def __init__(self,name, brand):
        self.wheels_count =6
        super().__init__(name,brand)
class Bike(Vehicle):
    def __init__(self,name, brand):
        self.wheels_count = 2
        super().__init__(name,brand)
        self.__reg_no = ''
        self.__owner = ''

    @property
    def reg_no(self):
        return self.__reg_no


    @reg_no.setter
    def reg_no(self,value):
       self.__reg_no= value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self,value:str):
        self.__owner = value


b = Bike('Apache RTR 200', 'TVS')
b.reg_no = 11223344
b.owner = 'John Doe'

print(b.reg_no)
print(b.owner)

print(issubclass(Bike,Vehicle))
print(isinstance(b,Vehicle))
print(isinstance(b,HeavyVehicle))