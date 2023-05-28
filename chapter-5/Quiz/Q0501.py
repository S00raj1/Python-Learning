num = [1,5,2,89,32,112,167,333,20,5,23]
odd =[]
even =[]
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print('even numbers are', even)
print('odd numbers are',odd)
