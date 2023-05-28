# Write a program to input a number from the terminal and check whether a number is an integer or not.

# number = int(input('Enter a number?'))
# if number == int(number):
#     print( "number is an integer")
# else:
#     print("number is not an integer")

# Write a program to input a word and find out if it is palindrome.

# text = input('enter a text:')
# rev = text[::-1]
# if text == rev:
#     print('text is palindrome')
# else:
#     print('text is not palindrome')

# Enter the temperature in celsius, and convert the temperature to fahrenheit. Finally, display different fever levels of the user.

# temp = int(input("Enter Temperature in celcius:"))
# fahrenheit = (((9/5)*temp)+32)
# if fahrenheit < 96:
#     print('the temperature is low')
# elif fahrenheit >= 96 and fahrenheit <= 98:
#     print('temperature is normal')
# elif fahrenheit >= 99  and fahrenheit <= 101:
#     print('patient has normal fever')
# elif fahrenheit >= 102 and fahrenheit <= 104:
#     print('patient has high fever')
# else:
#     print('patient is in critical condition')


# Write a program that accepts a number from the terminal and checks whether it is a multiple of both 3,4, and 5 or not
# number = int (input('enter a number'))
# if number / 4 ==0:
#     if number /3 == 0:
#         if number /5==0:
#             print('true')
# else:
#     print('false')



# Write a program that asks a user score in percentage and display the grade with some remarks as follows:
# Temperature 	Grade 	Remarks
# below 60% 	C 	Work hard otherwise you're going to fail the exam.
# 61% to 70% 	B 	Your result is satisfactory.
# 71% to 80% 	B 	Good Job, Keep doing better.
# 81% to 90% 	B 	Amazing Your hard work paid off.
# above 90% 	B 	Excellent work, Congratulations topper!!


marks = float(input('enter a number'))
if marks <= 60:
    print('Work hard otherwise youre going to fail the exam.')
elif marks >= 61 and marks <= 70:
    print('your result is satisfactory')
elif marks >= 71 and marks <= 80:
    print('good job, keep doing better')
elif marks >= 81 and marks <= 90:
    print("amazing your hard work paid off")
elif marks >= 91 and marks <= 100:
    print("excellent work, congratulations")