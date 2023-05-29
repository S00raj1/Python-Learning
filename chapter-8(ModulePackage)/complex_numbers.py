'''Complex number is a number with combination of real and imaginary part. It is denoted by a + ib where a is the real part of the number and b is the imaginary part. i is the representation of imaginary part. In python, we use the format (a + bj).

In python, complex numbers are builtin data type. We can perform complex operations without importing any external libraries but if we want to perform advanced calculations, we can use cmath library which comes along with python.'''
import math

x = 4 + 5j
y = 5j + 6
print(x+y)
print(type(x))
print(abs(x))
print(x.imag)



import cmath

x = 2 + 6j
print(cmath.polar(x))
print(cmath.rect(4,3))

a = 5
b = 10
print(complex(b,a)+complex(a,b))
print(math.pi)


a = 5 + 9j
print(cmath.phase(a))
print(cmath.log10(10))