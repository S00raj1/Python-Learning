# the range function
# using range() functions to iterate for 10 times

# for x in range(10):
#     print(f"the current value of x is: {x}")


# odd = list(range(1,20,2))
# print(odd)

# even = list(range(0,20,2))
# print(even)

#
# name = "hello world"
# name = name.upper()
# for char in name:
#     print(f'Ascii value of {char}:', ord(char))
#
#
# word ="change it into ascii code"
# word = word.upper()
# for x in word:
#     print(f'Ascii code for{x} is:', ord(x))

# odd = [1,3,5,7,9]
# double_odd =[]
# for num in odd:
#     double_odd.append(2*num)
# print(double_odd)
#
# even = [2,4,6,8,10]
# double_even = []
# for i in even:
#     double_even.append(i*2)
# print(double_even)
#
#
# prime = [2,3,5,7,11,13,17,19]
# double_prime = []
# for a in prime:
#     double_prime.append(a*2)
# print(double_prime)



# for loop with dictionary

# student = {
#     'name': 'Suraj',
#     'age' : '24',
#     'address' : 'biratnagar'
#  }
# for key, value in student.items():
#     print(f'The {key} is {value}')
#
#


#     for loop in nested loop

# nested = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in nested:
#     for j in i:
#         print(j,end='')
#
#
#



# lang = {
#     'low level': ['Machine Level', 'Assembly'],
#     'high level': ['C++', 'Java', 'Python']
# }
# for i in lang:
#     print(f'the {i} value are :')
#     for j in lang[i]:
#         print("          " +j)



# items = [chr(val) for val in range(65,70)]
# print(items)
#
# print(list(enumerate(items)))
#
#
#
#
# casts = ['Robert Downey Jr.','Scarlett Joahnsson','Chris Evans','Mark Ruffalo','Chris Hemsworth']
# for index, cast in enumerate(casts):
#     print(f'{index}\t{cast}')

#
# casts = ['Robert Downey Jr.','Scarlett Joahnsson','Chris Evans','Mark Ruffalo','Chris Hemsworth']
# character = ['Iron Man','Black Widow','Captain America','Hulk','Thor']
# print(list(zip(casts,character)))
#
#
# for cast, character in zip(casts,character):
#     print(f'-{cast} played as "{character}"in Avenger')
#


student = ['Suraj','Himal','Shardul','Saiman','Dipesh','Shashank']
Department = ['Backend','Backend','Ui/Ux','Full stack','QA','Ui/ux']
salary = [50,70,80,90,50,40]

# for i in zip(salary,student,Department):
#     print(i)


# for student, Department, salary in zip(student,Department,salary):
#     print(f'-- {student} does {Department} development in Cagtu and gets {salary}k')

#
for i in zip(student,Department,salary):
    print (i)

