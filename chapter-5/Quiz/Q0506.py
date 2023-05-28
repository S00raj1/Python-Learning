'''*
*   *
*   *   *
*   *   *   *
*   *   *   *   *'''
# for x in range(0,5):
#     for y in range(0,x+1):
#         print('*',end="")
#     print()


'''1
1   3
1   3   5
1   3   5   7
1   3   5   7   9'''

# for x in range(1,10):
#     if x % 2 != 0:
#         for y in range(1,x+1):
#             if y % 2 != 0:
#                 print(y,end="  ")
#     print()

'''1
2   2
3   3   3
4   4   4   4
5   5   5   5   5'''

# for x in range(1,6):
#     for y in range(1,x+1):
#         print(x,end="  " )
#
#     print()

'''1
2   1
3   2   1
4   3   2   1
5   4   3   2   1'''

# for x in range(1,6):
#     for y in reversed(range(1,x+1)):
#         print(y,end=" ")
#     print()


'''1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25'''


# for x in range(1,6):
#     for y in range(1,6):
#         y = y * x
#         print(y,end='  ')
#
#     print()

'''A
A   P
A   P   P
A   P   P   L
A   P   P   L   E'''

# word = 'APPLE'
# for i in range(0,5) :
#     for j in range(0,i+1):
#         print(word[j], end="  ")
#
#     print()

'''             *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *'''


# for x in (range(0,6)):
#     print('   '* (5-x),end="")
#     for y in (range(x,0,-1)):
#
#         print("*",end="  ")
#
#     print()


'''             1
            1   3
        1   3   5
    1   3   5   7
1   3   5   7   9'''

for x in range(1,6):
    print("    "*(5-x),end="")
    if x % 2 != 0:

        for y in range(1,x+1):
            print(y,end="   ")
    print()


