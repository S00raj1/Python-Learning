person = {
    'name' : 'Suraj',
    'age' : 24,
    'profession' : 'IT',
    'married' : False
}

# print(person['name'])
person['age'] +=10
print(str(person))
# print(person[''])

print(person.get('employed'))
print(person.get('employed',False))