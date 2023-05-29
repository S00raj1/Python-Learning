# a = 10
# b = 0
# try:
#     print(a/b)
# except:
#     print('Hello world')
import math


# def add(a,b):
#     try:
#         # print('hello world!! i am trying to divide a with b')
#         x = (int)(a) / b
#         return x
#     except ZeroDivisionError:
#         print("This statement is printed only if the zero division error occurs")
#     except TypeError as e:
#         print("This statement is printed only if the typeerror occurs while executing")
#     except Exception as e:
#         print("This statement is printed only if the unknown error occured")
#
#
#
# add("l",'aa')



# list_1 = [6,8,9,"HArry",'Broke']
# def print_index(index:int):
#     value = None
#     try:
#         value = list_1[index]
#     except IndexError:
#         print('There is an error, the index is out of range, the last value would be printed')
#         value = list_1[-1]
#     else:
#         print("ther is no error")
#     finally:
#         print(f'all errors are handled here. the value is {value}')
# print_index(5)
# print_index(2)

def div(a,b):
    try:
        x= a/b
    except(TypeError,ZeroDivisionError):
        print("Error is spotted here")

    else:
        print('hello world')
div(1,0)
div(10,5)