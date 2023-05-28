import math

number = int(input('enter a number'))
sum = 0
ones = number %10
tens = number //10
x = tens %10
hundreds = tens //10
print(ones)
print(x)
print(hundreds)
ones = math.factorial(ones)
x= math.factorial(x)
hundreds= math.factorial(hundreds)
sum = ones + x+ hundreds
print (sum)
if number == sum:
    print(f'{number} is a special number')
else:
    print(f'{number } is not a special number')