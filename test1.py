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

'''code to find weird or not werid by if else'''
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
