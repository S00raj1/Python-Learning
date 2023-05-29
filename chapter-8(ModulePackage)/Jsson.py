import json
'''
    JSON (JavaScript Object Notation) is a light weight data interchange format inspired by Javascript object literal syntax.
    A JSON file contains an object or an array that can contain different levels of nesting.
    Keys are string and are surrounded with double quotes ".
'''

'''
Json Basic Example:
{
    "name" : "John Doe",
    "age" :  20,
    "married" : True,
    "children" : null
}
'''
'''
Json example with nested objects:
{
    "name" : "grade 1",
    "session" : 2022,
    "class_teacher" : "John lennon",
    "students" : [
        {
            "id" : 1,
            "name" : "John Doe",
            "subjects" : ["Physics","Mathematics"]
        },
        {
            "id" : 2,
            "name" : "Jane Doe",
            "subjects" : ["Chemistry ", "Biology"]
        }
        
    ]
}
'''


"""Dumping Python Dictionary into a json string or a file"""
# person = {
#     "name" : "Suraj Rajbanshi",
#     'age' : 24,
#     'married' : False,
#     'occupation' : 'programmer',
#     'programming_languages' : [
#         {
#             'name' : 'Python',
#             'version' : 3.9,
#             'level' : 'Expert'
#         },
#         {
#             'name': 'Java',
#             'version' : 17,
#             'level' : 'Expert'
#         },
#         {
#             "name" : "c++",
#             "version" : 2019,
#             "level" : "Mid"
#         }
#     ]
# }
# with open('Json.json','w') as f:
#     json.dump(person,f)


# Dumping the dictionary into json string
# import json
# json_str =json.dump(person)

# Dumping the dictionary into JSON file




# students ={
#     "name" : 'Himal Subedi',
#     "age" : 21,
#     "course " : 'BSC CSIT',
#     "Address" : 'Biratnagar',
#     "skills" :
#         [
#             {
#                 "name" : "Frontend Designing",
#                 "Skills " : ['HTML','CSS','JS','ReactJS','NextJS']
#             },
#             {
#                 "name" : "Backend Developer",
#                 "skills" : ['Javascript','NodeJS','Python','Django']
#             }
#
#         ]
# }
#
# with open("himalss.json", "w") as f:
#     json.dump(students,f)




player = [
            {
            "name" : 'Paras Khadka',
            "age " : 38,
            "game" : "Cricket"
            },
            {
            "name" : "Sandip Lamichhane",
            "age" : 25,
            "game" : "Cricket"
            },
            {
            "name" : "Kiran Chemjong",
            "age" : 34,
            "game" : 'Football'
            }
]


with open("Sports.json" , "w") as f:
    json.dump(player,f)



# json_string = '{"name":"Kiran Chemjong","age":34,"game":"football"}'
# dict_1 = json.loads(json_string)


with open("Sports.json",'r') as file:
    dict_1 = json.load(file)
    print(dict_1)


with open("himalss.json",'r') as filee:
    xyz = json.load(filee)
    print(xyz)
