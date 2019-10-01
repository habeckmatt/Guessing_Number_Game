import math
from math import degrees

# Addition Operation

a1 = float(input('Addition. Enter first number '))
a2 = float(input('Enter second number '))
a3 = a1 + a2

print(a1, '+', a2, '=', a3)

# Subtraction Operation

s1 = float(input('Subtraction. Enter first number '))
s2 = float(input('Enter second number '))
s3 = s1 - s2

print(s1, '-', s2, '=', s3)

# Multiplication Operation

m1 = float(input('Multiplication. Enter first number '))
m2 = float(input('Enter second number '))
m3 = m1 * m2

print(m1, '*', m2, '=', m3)

# Division Operation

d1 = float(input('Division. Enter first number '))
d2 = float(input('Enter second number '))
d3 = d1 / d2

print(d1, '/', d2, '=', d3)

# Modulous Operation

mod1 = float(input('Modulous. Enter first number '))
mod2 = float(input('Enter second number '))
mod3 = mod1 % mod2

print(mod1, '%', mod2, '=', mod3)

# Square Root Operation

sq1 = float(input('Square Root. Enter the number to take the square root of '))

sq2 = sq1 ** (1/2)

print(sq1, '**', '1/2 =', sq2)

# Exponentiation Operation

e1 = float(input('Exponentiation. Enter a number for the "base" 10 '))
e2 = float(input('Enter the power '))
e3 = e1 ** e2

print(e1, '^', e2, '=', e3)

# SOHCAHTOA

r1 = float(input('Enter number to compute sin, cos, and tan of '))

r2 = math.sin(r1)
r3 = math.cos(r1)
r4 = math.tan(r1)

r5 = (degrees(r2))
r6 = (degrees(r3))
r7 = (degrees(r4))

print(r2)
print(r3)
print(r4)


# Logarithm

l1 = float(input('Logarithm. Enter the value of x '))
l2 = float(input('Enter the base '))

l3 = math.log(l1,l2)

print('Log base', l2 , 'of', l1 , '=' , l3)
