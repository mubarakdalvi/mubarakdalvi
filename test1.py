import math
import os
import random
import re
import sys

'''Code for add, sub , multiply'''

a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

'''code to find weird or not weird by if else'''
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
'''code to  find floor division and division'''
a = int(input())
b = int(input())
print(a // b)
print(a / b)

"""using for loop for finite times multiplying number"""
i = int(input())
for n in range(0, i):
    if n <= i:
        print(n ** 2)
"""to find leap year"""
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    leap = False
    return leap

year = int(input())
print(is_leap(year))

'''code for using import re method to find str in variable '''
# no trouble
a = 'i am in pune and i am in maharashtra and also i am in india'
b = ['i', 'am', 'pune', 'and', 'maharashtra', 'india', 'also', 'in']
for x in b:
    print('Searched For : ', x, 'and found:', re.findall(x, a))

# code for checking repeating alphabets
s = '....abf....'
v = re.findall('a+b+', s)
print(v)
# code for using try except and finally in to check a is = to b or not via re module and findall () method
try:
    a = 'i am  Pune'
    b = 'i Pune'
    print(re.findall(b, a))
    if a == b:
        print('Yeah Its a Match')
    else:
        print('No its not a match')
except:
    print('Ahh Here We Go Again')
finally:
    print('thank for taking part')

