'''A A A A A
A A A A A
A A A A A
A A A A A
A A A A A'''

# for x in range(5):
#     for y in range(5):
#         print('A',end="")
#
#     print()

'''1
1	2
1	2	3
1	2	3	4
1	2	3	4	5'''

# for x in range(1,6):
#     for y in range(1,x+1):
#         print(y, end='')
#     print()

'''1
2  2
3  3  3
4  4  4  4
5  5  5  5  5'''

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(i,end="")
#     print()

'''            1
         2  1
      3  2  1
   4  3  2  1
5  4  3  2  1'''


for i in range(1,6):
    print("     "*(5-i),end="")
    for j in range(i,0,-1):
        print(i,end="    ")
    print()
