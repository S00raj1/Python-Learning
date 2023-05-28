# a = 20
# b = 25
# if a > b:
#     print('{} is greater then {}'.format(a,b))
# print('{} is greater then {}'.format(b,a))



# a = input('Enter your age')
# if int(a) > 18:
#     print('you are elisible for voting')
# elif int(a) == 18:
#     print('you are elisible for voting')
# else:
#     print('you are not elisible for voting')


# number =  int(input('Enter a number?'))
# match number:
#     case 1: 
#         print('it is the first natural number')
#     case 7:
#         print('it is the luckiest number')
#     case 10:
#         print('it is messi jersey number')
#     case _:
#         print('these are the random number')



# day =input('Enter a day?')
# match day:
#     case ('sunday'):
#         print('This is the first day of week')
#     case ('monday'):
#         print('this is the second day of week')
#     case ('tuesday'):
#         print('this is the third day of week')
#     case ('wednesday'):
#         print('this is the fourth day of week')
#     case ('thrusday'):
#         print('this is the fifth day of week')
#     case ('friday'):
#         print('this is the sixth day of week')
#     case ('saturday'):
#         print('this is the last day of week')
#     case _:
#         print('invalid day ')



# (a,b) = (int(input('Enter a number?')),int(input('enter a number?')))
# match (a,b):
#     case (0,0):
#         print('this point lies in origin')
#     case (0,b):
#         print('this point lies on x-axis')
#     case(a,0):
#         print('this point lies on y axis')
#     case(a,b):
#         print('this point lies somewhere')






number = int(input("Enter a number?"))
if number > 50:
    if number % 2 == 0:
        print('number is even')
    else:
        print('number is odd')

else:
    if  number % 2 ==0:
        print('smaller number is even')
    else:
        print('smaller number is odd')