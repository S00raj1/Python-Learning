# sum of first n natural numbers
# n = int(input('enter a number'))
#
# def natural(n):
#     sum = 0
#     for i in range (1,n+1):
#        sum += i
#     print(sum)
#
# natural(n)
#

# factorial of a non-negative number
# num = int(input('enter non negative number'))

# def fact(num):
#     if num > 0:
#         factorial = 1
#         for i in range (1,num+1):
#             factorial = factorial * i
#         print(factorial)
# fact(num)

# sum of digits of the number
#
# number = int(input('enter a number::'))
# def sum(number):
#     summ = 0
#     for digit in str(number):
#         summ += int(digit)
#     print(summ)
# sum(number)

# print the nth element of the fibonacci series [1, 1, 2, 3, 5, 8, 13, 21,...]

num = int(input('enter a number:'))
def fibonacci(num):
    a = 0
    b = 1
    for i in range (1,num+1):
        sum = a + b
        b = a
        a = sum
    print(sum)
fibonacci(num)