'''def add_numbers(a,b,*args): #after initializing args we can pass multiple value
    sum_value = a+b
    for item in args:
        sum_value += item
    return sum_value
print(add_numbers(2,4))
print(add_numbers(2,4,6,8,9))
print(add_numbers(2,4,10,11,9))
print(add_numbers(2,4,3))
'''

# def subtract_number(a,b,*args):
#     diff_value = a-b
#     for item in args:
#         diff_value -= item
#     return diff_value
# print(subtract_number(5,10))
# print(subtract_number(5,10,7,10,9))
# print(subtract_number(5,10,12))
#
#
# def divide_number(a,b,*args):
#     divide_value = a/b
#     for item in args:
#         divide_value /= item
#     return divide_value
# print(divide_number(5,2))
# print(divide_number(5,2,10))
# print(divide_number(5,2,12,14))



# Arbitary number of keyword arguments
# def display_student_detail(name,age,**kwargs):
#     print(f'[details of {age} years old student: {name}]')
#     for key,value in kwargs.items():
#         print(f'The {key} is {value}')
# display_student_detail(
#     'John Doe',20,
#     subject = 'Science',class_teacher = 'Johna Lennon', address = 'Singapore'
# )
#


'''def display_contact(name,**kwargs):
    print(f'Welcome {name}')
    for key,value in kwargs.items():
        print(f'the {key } is {value}')
display_contact(
    'John Doe',
    phone = 98120000,phone_1 = 9712000,phone_2 = 965200
)'''

'''def college_details(name,semester,**kwargs):
    print(f'Welcome {name}, your semester is {semester}')
    for key,value in kwargs.items():
        print(f'the {key} is {value}')
college_details(
    'Suraj Rajbanshi','Eight',
    intern='Cagtu', department='backend'
)'''

def hostel(name,location,**kwargs):
    print(f'Welcome to {name} hostel located at {location}')
    for key,value in kwargs.items():
        print(f'It has {value} {key}  ')
hostel(
    'Namuna Boys','Thapagaun',
    floor = 6, students = 70
)





