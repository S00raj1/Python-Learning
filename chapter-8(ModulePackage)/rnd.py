import random

# s=random.randint(1,10)
# # print(s)
# print(random.randrange(0,8,2))
# if int(input('Enter your number:')) == random.randrange(0,8,2):
#     print('you are pro')
# else:
#     print('Go and study ')
#

options = '123456789ABCDEabcde@#$%&'
print(''.join(random.choices(options,k=10)))