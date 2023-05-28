x = int(input('Enter a number:'))
def line_equation():
    if x %2==0 and x%3 == 0:
        print(x**3+(4*x)**2+5*x+6)

    elif x %3 == 0:
        print(x**3+4*x+5)
    elif x % 2 == 0:
        print( x**2 + 2*x+3)
    else:
            print(-(x))

line_equation()
