a = (1,2,3,4,5)
print(len(a))
i = a.index(2)
l= a[2]
print(l)
print(a[4])
b = (6,7,8,9)
a= a+b
print (a)
a= (*a,*b)
print(a)
print(len(a))
x=enumerate(a,start =2)
print(list(x))
