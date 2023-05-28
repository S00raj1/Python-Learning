# # nesting of list and tuple
# nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# nested_tuple = (('x','y','z'),('a','b','c'))


# # nested dictionary
# person ={
#     'name' : 'John',
#     'age' : 20,
#     'company' : {
#         'name' : 'microsoft',
#         'established' : 2070,
#         'location' : ['Xyz','yyz']
#     }
# }
# print(person)


# # nesting between different data types
# students = [
#     {
#         'name':'John Doe',
#         'age' : 20,
#         'majors':('mathematics','nepali')
#         },
#     {
#         'name':'Jane Doe',
#         'age' : 22,
#         'majors' : ('biology','physics')
#     }
# ]

# print(students)

# for i in students:
#     print('the length of dictionary is :',(str)(len(i)) +" " +  'the dictionary is :',str(i))



# # Accessng items from the nested iterable 

# intern = {
#     'name' : 'Suraj',
#     'designation' : 'intern',
#     'department' : 'backend',
#     'qualification': ['Python',
#                       'javascript',
#                       'Php',
#                       'java'
#                       ],
#     'frameworks' :{
#         'Javascripts' : 'nodejs',
#         'python' : 'django'
#     }
# }

# print(intern)

# print(intern['qualification'],intern['frameworks']['Javascripts'])



# college ={
#     'name' : 'Biratkshitiz',
#     'faculty' : {
#         'bca' : ['first','second','third','fourth','fifth','sixth','sevent','eight'],
#         'csit' : ['first','second','third','fourth','fifth','sixth','seventh','eight']
# },
#     'students' : 100,
#     'class' : 8
# }
# # print(f'the length of dictionary is {len(college)}  {college["name"]} { college["faculty"]["bca"]}')
# # print('the length of dictionary is ',str(len(college)) + college['name'] + (str)(college["faculty"]['csit']))

# college['students'] = 150
# print(college)
# college['faculty']['bca'][2] = 'change'
# print(college)




students = [
    {
        'name' : 'Suraj',
        'caste' : 'Rajbanshi',
        'Address' : 'Biratnagar'
     },

    {
        'name' : 'Himal',
        'caste' : 'Subedi',
        'Address' : 'Biratnagar'
     },

    {
        'name' : 'Saiman',
        'caste' : 'Khatiwada',
        'Address' : 'Biratnagar'
     },

    {
        'name' : 'Cag',
        'caste' : 'Tu',
        'Address' : 'Biratnagar'
     },
]

for i in (students):
  for j in i.items():
   print(*j)


new_student = {
  'name' : 'Hom',
  'caste' : 'maley',
  'Address' : 'Biratnagar'
}
students.append(new_student)
print(students)