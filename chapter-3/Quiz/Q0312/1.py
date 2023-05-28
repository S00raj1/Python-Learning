PI:float = 3.1415
PI =int(PI)
print(PI)

str_1 = '20'
str_2 = '30'
print(int(str_1)+int(str_2))

x = [ '1','2','3','4','5']
sum = 0
for i in x:
    sum = sum+int(i)
print(sum)

odd = [1,3,5,7,9,11,13,15]
prime = [2,3,5,7,11,13,17]

print(set(odd) - set(prime ))

print(set(odd)^set(prime))

print(set(prime)-set(odd))

