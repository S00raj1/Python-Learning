number = int(input('enter a number'))
factor = []
while number < 1:
    print('number is smaller then 1')
    break
else:
    for i in range(1,number+1):
        if number % i==0 :
            factor.append(i)

    print(factor)