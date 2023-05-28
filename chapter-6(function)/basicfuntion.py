# def my_function():
#     print('hello world!!!')
#
# print('hey world! i am outside of the function')
#
# my_function()
# my_function()


# the return statement

# def say_hello():
#     return 'Hi there'
# x = say_hello()
# print(x)


# msg = input('Enter your name?')
# def say_hello():
#     return f'hello {msg}, welcome to CagtuNepal'
# print(say_hello())
#
#
# first_number = int(input('enter first number?'))
# second_number = int(input('enter second number?'))
# sum = 0
# def addition():
#     sum = first_number + second_number
#     return sum
#
# x = addition()
# print('sum =',x)
#
#
# def subtraction():
#     difference = first_number - second_number
#     return difference
# print('subtraction is :',subtraction())

# function with arguments


# def add_me (num1,num2):
#     return num1+num2
# result = add_me(first_number,second_number)
# result_1 = add_me(50,40)
#
# print('the result with user input data is ' , result)
# print('the result with static data is' , result_1)


# Example 2: A function that finds out the simple interest along with type hinting
# def simple_interest(principal:int, time:int, rate:float)->float:
#     SI = (principal*time*rate)/100
#     return SI
# si = simple_interest(100,20,0.5)
# print(si)



# p = float(input('Enter a principal:'))
# t = int(input('Enter a time:'))
# r = float(input('Enter a rate:'))
#
# def simple_interest(p:float,t:int,r:int)->float:
#     return (p*t*r)/100
# si = simple_interest(p,t,r)
# print(si)

# Example 3: A function that has loop inside it

# def print_multiple(value,iteration):
#     for x in range(1,iteration+1):
#         print(f'iteration {x}:',value)
# print_multiple('Hello There',5)

# number = int(input('Enter a number of times you wanna prints:'))
# msg = input('Enter a msg you wanna print')
# odd_msg = input('Enter odd msg you wanna print')
# def print_value(x,iteration):
#     for i in range(1,number+1):
#         if i % 2 == 0:
#             print(f'{msg}',i)
#         else:
#             print(f'{odd_msg}',i)
# print_value(msg,number)
#



# Example 4: A function that returns the double of a number if it is even and triple of a number if it is odd.

# number = int(input('Enter a number:'))
# def check(num):
#     if num % 2 == 0:
#        return print('number is even so we double the number:', num*2)
#     else:
#         return print('number is odd so we triple the number:', num*3)
#
#
# check(number)


# Local, Non-local and Global variables

# p = 10
# def check():
#     x = 10
#     print(p)
#     print(x)
#
# check()
# # print(x)


#
# message = 'Hello World'
# def msg():
#     print(message)
#
# msg()
# print(message)


# The global keyword
# x = 'Hello World'
# print(x)
# def my_function():
#     global x
#     x= 'hi there'
# my_function()
# print(x)
# print(x)


# x = 10
# def outer_function():
#     x = 20
#     def inner_function():
#         nonlocal x
#         x += 10
#         print(x)
#     print('the value off xx is :', x)
#     inner_function()
#     print('the value of x is:',x)
# outer_function()
# print(x)



a = 15
def outer_function():
    a = 20
    def inner_function():
        nonlocal a
        a += 20
        print('the main inner function value of a is:',a)
    print('the value of unchaged local value of a is :', a)
    inner_function()
    print('the value of a is changed after innerfunction is distroyed:',a)
outer_function()
print('the value of a as global variable is  :',a)
