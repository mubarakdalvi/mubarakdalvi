import cmath
from cmath import phase
z = complex(input('Enter Number : '))
r, phi = cmath.polar(z)
print(f'{r:.15f}')
print(f'{phi:.16f}')