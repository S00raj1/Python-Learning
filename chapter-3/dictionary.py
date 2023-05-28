student = {
    'name' : 'suraj',
    'grade' : '8th semester',
    'position' :['Intern','Frontend','backend']
   
}
student1 = {
    'name' : 'himal',
    'grade' : '8th semester',
    'position' : ['Intern','Frontend','backend']
}
# print(student.keys(), student.values(),student.items())

# student2= student.copy()
# print(student2)
student3 = student.fromkeys(student1)
print(student3)
student3 = student3.clear()
print(student3)

# (key,value) = student1.popitem()
# print(key,value)
# print(student,student1)
# print(student['grade'])
# print(student1['position'])

# student['skills'] = ['html','css','js','python']
# print(student)


# student1['languages'] =['English','Nepali','Hindi']
# print(student1)


# student1['name'] = 'suraj'
# print(student1)




# frontend = {
#     'name' : 'Siraj ',
#     'college' : 'Biratkshitiz',
#     'profession' : 'Teacher',
#     'subject' : ['E-commerce','DBMS','OOP']
# }

# for i in frontend:
#     print (i +" : " + (str)(frontend[i]))
#     # print (frontend[i])

# backend = {
#     'age' : 25,
#     'height' : 5.7,
#     'weight' : 50
#  }
# frontend.update(backend)
# print(frontend)

# for i in backend:
#     print(i + ":" + str(frontend[i]))
# backend.pop('age')
# print(backend)
# frontend.pop('name')
# print(frontend)

# (key, value) = frontend.popitem()
# print(key,value)