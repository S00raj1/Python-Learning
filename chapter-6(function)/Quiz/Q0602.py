# Write a python function that calculates the number of upper case characters, lower case characters and spaces in the string and returns them as a tuple.

sentence = input('Enter a sentence')

def check(sentence):
    up = 0
    down = 0
    space = 0
    for i in sentence:

         if i.isupper():
            up += 1
         if  i.islower():
            down += 1
         if i.isspace():
            space += 1
    count = (up, down, space)
    print('count =', tuple(count))
check(sentence)


