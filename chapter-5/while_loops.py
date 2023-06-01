# x = 10
# while x  <=20:
#     print('Hello World')
#     x += 1
# print('the loop is completed')



# y = 1 
# while y <= 10:
#     print('the value of x is:',y)
#     y += 1
# print('the loop is completed')


# Write a program that inputs names of students until the user enters exit and display the list at the end.
# name_list= []
# name = ''
# while name.lower() != 'exit':
#     name=input('enter your name:')
#     name_list.append(name)
# print(name_list[:-1])

# name_list = []
# name = ''
# while name.lower() != 'exit':
#     name = input('enter your name:')
#     name_list.append(name)
# print(name_list[:-1])

# x = -1
# while x <= 10:
#     print('the number is :',x)
#     x += 1
# else:
#     print('number is not smaller then 10')


# x = int(input('enter your age:'))
# while x <=20:
#     x += 1
#     if x == 2:
        
#         continue
#     else:
#         print('age is',x)


# Example 2: Write a program that displays all words entered by the user.
# offensive = ['dull','ugly','short']
# highly_offensive = ['dog','shit','damn','beat']

# while True:
#     word = input('enter a word:')
#     if word in offensive:
#         print(f'the word{word[0]}{"*" * (len(word)-1)}is offensive so skipping execution')
#         continue
#     if word in highly_offensive:
#         print ('Your word is highly offensive, good bye')
#         break
#
#     if word == word[::-1]:
#         print(f'the word {word}is in palindrome')
#     else:
#         print(f'the word {word} is not in palindrome')

# n = 4
# while n <=6 :
#     mul = 1
#     while mul <= 10:
#         print(f"{n} X {mul} = {(n * mul)}")
#         mul += 1
#     print()
#     n += 1




#
# a = 5
# while a <=10:
#     b = 1
#     while b<=10:
#         print(f'{a:>2}  X {b:>2}  =  {(a* b):>2}')
#         # print(f'the multiplication of {a} and {b} is : {a * b}')
#         b += 1
#     print()
#     a +=1


import time
hour = 0
while hour < 12:
    minute = 0
    while minute < 5:
        seconds = 0
        while seconds < 50:
            time.sleep(1)
            current_time = f"Time Elapsed : {hour:0>2} : {minute:0>2} : {seconds:0>2}"
            print('\r',current_time, end='')

            if hour == 00:
                if minute == 00:
                    if seconds == 00:
                           seconds += 1
        minute += 1
    hour += 1


