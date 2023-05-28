# lst =[ 2*x+1 for x in range(10) ]
# print(lst)
#
# list_1 = {key: key**2 for  key in range(1,10)}
# print(list_1)
#
#
#
# list_3 = {key:key**3 for key in range(2,5)}
# print(list_3)
# list_4 = {key:key/3 for key in range(2,10)}
# print(list_4)
#
#
# pattern = [ print() or [print(y, end="  ")  for y in range(1,x+1)] for x in range(1,6)]

# A mathematical function is defined by y = 4x ** 2 + 3x - 6
#
#     Create a generator function to generate first 1000 integers starting from -100 and store to a variable y.
#     Create a list using list comprehension to generate the same values
#     Compare the memory usage by those variables created in steps i and ii using __sizeof__() method.
#     Try to generate values of y for first million integers and compare memory usage as done in step iii.


# generator = ((4*x ** 2 + 3*x - 6) for x in range(1000))
# print(generator)
#
# list = [4*x **2 + 3*x - 6 for x in range(-100,1000)]
# print(list)
# print(list.__sizeof__())
#
#
# lists = [4*x **2 + 3*x - 6 for x in range(10000)]
# print(lists.__sizeof__())
#
#
#


#
# word = 'Apple'
# xyz = {key:ord(key) for key in word}
# print (xyz)


abbreviations = (
    ('ABC', 'Atanasoff Berry Computer'),
    ('BCD', 'Binary Coded Decimal'),
    ('CD', 'Compact Disc'),
    ('DVD', 'Digital Video Disc'),
    ('HTTP', 'Hyper Text Transfer Protocol'),
    ('WWW', 'World Wide Web'),
)

xyz = {key:value for key,value in abbreviations}
print(xyz)