a = [1,2,3,4,5,6,7,8]
print('original list' ,a)
b = a
print('original list of b', b)
b.pop()
print('the value of b after pop operation',b)
print('the value of a after pop operation ',a)



# using copy method
a = [1,2,3,4,5,6,7,8]
print('original list' ,a)
b = a.copy()
print('original list of b', b)
b.pop()
print('the value of b after pop operation',b)
print('the value of a after pop operation ',a)
