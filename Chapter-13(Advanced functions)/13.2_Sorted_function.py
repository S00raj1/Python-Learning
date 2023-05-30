# number = [1, 2, 5, 4, 3, 10, 11, 9, 7, 6, 8]
# number = sorted(number)
# print(number)
#
# number = sorted((number), reverse=True)
#
# print(number)

student = {
    "name": "Suraj_Rajbanshi",
    "age": '24',
    "address": 'Biratnagar_08',
    "temporary_address": 'Kathmandu_Kalopul'
}
#
# student = sorted(student)
# print(student)

for key,values in sorted(student.items()):
    print(key,"-",values)


print(sorted(student.items()))



students = [
    ('Suraj',1),
    ('Himal',2),
    ('Shardul',3),
    ('Dipesh',4),
    ('Shlok',5)
]

print(sorted(students,key= lambda x:x[0]))