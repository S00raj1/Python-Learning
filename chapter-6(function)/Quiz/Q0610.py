# A lambda function that accepts a number and returns the square of it.
# '''num = int(input('Enter a number'))
# square = lambda num: num**2
# print(square(num))'''

# A lambda function that accepts a list of numbers and returns the list of squares of them
# a = []
#
# while True:
#     b = int(input('enter a number::'))
#     a.append(b)
#     check = input('do you wanna give more input? [yes/no]')
#     if check == 'no':
#         break
# c= lambda a: print([i*i for i in a])
# (c(a))


# A lambda function that accepts the length in meter and returns the value in feet.
# length = int(input('enter a length in meter::'))
# a = lambda length: length*3.2
# print(a(length))

# A lambda function that accepts 3 integer arguments for month, year, and day, and returns a single string in format YYYY/MM/DD format.
import dateutil
# year = int(input('enter year'))
# month = int(input('enter month'))
# day = int(input('enter day'))
#
# xyz = lambda year,month,day : print(f'{year}/{month}/{day}')
# xyz(year,month,day)


# A lambda that accepts a sentence and returns the sentence with spaces replaced by hyphens.
#
# # example
# input_sentence = 'A quick brown fox jumps over the lazy dog.'
#
# output_sentence = 'A-quick-brown-fox-jumps-over-the-lazy-dog.'


sentence = 'A quick brown fox jumps over the lazy dog.'
# result = lambda sentence: sentence.replace(' ','-')
result = lambda sentence: ('-'.join(sentence.split(' ')))
print(result(sentence))