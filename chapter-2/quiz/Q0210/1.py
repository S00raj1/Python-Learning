a = 12
if a == int(a):
    print('a is an integer')
else:
    print('a is not integer')


b = 100 / 12
if b ==  int(b):
    print('remainder is an integer')
else : 
    print('remainder is a float')

x = [1,2,3,4,5]
y = [1,2,3,4,5]
z = x
if x == y:
    print('x is identical to y')
else:
    print('x is not identical to y')

if x == z:
    print('x is identical to z')
else:
    print('x is identical to z')


p = ['elephant','tiger','zebra','lion','wolf']
if p.index('lion'):
    print('lion is in zoo')
else:
    print('lion is not in zoo')

'''try:
    if p.index('horse'):
        print('xyz')
except:
    print('horse is not in zoo')
'''

if 'horse' in p:
    print('horse is in zoo')
else:
    print('horse is not in zoo')


p = [2,3,5,7,11,13,17]
if 9 in p:
    print('9 is a prime number')
else:
    print('9 is not a prime number')