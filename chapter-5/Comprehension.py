# new_list = []
# for x in range(1,11):
#     new_list.append(x+2)
# print(new_list)
# list_1 =[x*2 for x in range(1,11)]
# print(list_1)
# list_2 =[x /2 for x in range(1,11)]
# print(list_2)
#
#

# text = 'hello world'
# x = [ord(char) for char in text]
# print(x)
#
# x = range(70,80)
# y = [chr(ascii) for ascii in x]
# print(y)
#
# a = range(40,70)
# b = [chr(ascii) for ascii in a]
# print(b)
#
# numbers = [1,2,3,4,2,5,6,7,8,9,1,0,10,12,11,13,14,15,16,17,18,19,20]
# even = [num for num in numbers if num%2 == 0]
# odd = [num for num in numbers if num%2 != 0]
# print(even,odd)

# set compression
# x = {1,2,3,4,5,3,7,2,5,10,11,1,2,12,13,14,15,16,17,18,19,20}

# x= list(x)
# print(x)
# y={ num for num in x if num%2==0}_
# print(y)

# for dictionary
# dictionary = {key:key**2 for key in range(1,6)}
# print(dictionary)
#
#
#
# dictionary_1 = {key:key/2 for key in range (10,20)}
# print(dictionary_1)

# using list comprehension
squares_1 = [x ** 2 for x in range(1000)]
print(squares_1.__sizeof__())


sqr = [x ** 3 for x in range(1000000) ]
print(sqr.__sizeof__())

#
# sqr_1 = (x ** 2  for x in range(1000))
# print(sqr_1.__sizeof__())
# sqr_2  = (x ** 2  for x in range (1000000))
# print(sqr_2.__sizeof__())

# Using Generator Comprehension to get first 1000 squares
squares = (x ** 2 for x in range(1000))
print(squares.__sizeof__())

# Using Generator Comprehension to get first 1000000 squares
squares_1 = (x ** 2 for x in range(1000000))
print(squares_1.__sizeof__())