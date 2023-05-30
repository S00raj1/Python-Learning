import re
abc = 'John,Jane,Jennifer,Joan,Jon,Adam,Eve'
print(re.findall(r'J\w*n',abc))


print(re.search(r'J\w*r',abc))

word = "The world is full of demons.The winter is comming. Get out of my room. You are not invited to the party"
print(re.findall(r'd\w*s',word))

numbers = 9810001010,9812124545,9817161715,97564851641
print(re.findall(r'[98]\d{4}',str(numbers)))