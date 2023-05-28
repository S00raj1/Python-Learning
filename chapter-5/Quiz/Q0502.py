
a=0
b =1
d=[]
for i in range (20):
    c= a+b
    b= a
    a = c
    d.append(c)
print(d)