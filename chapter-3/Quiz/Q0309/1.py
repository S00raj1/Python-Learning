car = {
    'brand' : 'Hyundai',
    'model' : 'xyz120',
    'price' : 10000000

}
car['engine'] = 1200
print(car)

car['color'] = 'red'
car['no_of_seats'] = 5
car['transmission'] = 'dont know'
print(car)
car.pop('color')
print(car)
(key , values) = car.popitem()
print(key,values)


for i in car:
    print (i)

for i in car.keys():
    print(i )
for i in car.values():
    print(i)
for i in car.items():
    print(i)