'''def factorial(n):
    if n>0:
        return n * factorial(n-1)
    return 1
print(factorial(7))


n = int(input('Enter a number:'))
def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    return 1
print(factorial(n))
'''


# A recursive function that prints out the first nth item of a fibonacci series 1, 1, 2, 3, 5, 8, 13, 21, 34, ....
'''def fibonanci(n):
    if n > 1:
        return (fibonanci(n-1))+fibonanci(n-2)
    return n
item = fibonanci(7)
print(item)
'''

def dec(n:int):
    if n != 0:
        return dec(n//2)*10+n%2
    else:
        return 0
print(dec(14))
