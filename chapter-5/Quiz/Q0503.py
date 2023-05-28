x = list(range(100))
print(x)
l = x
sum = 0
sqr= 0
y = 0
for i in x:
    sum = sum+i
    x = i **2
    sqr = sqr +x
    # y =( i ** 2) +(2*i)+2
    y=(i**2+2*i+2)+y
    avg = sum/len(l)
print(sum)
print(sqr)
print(y)
print(float(avg))
