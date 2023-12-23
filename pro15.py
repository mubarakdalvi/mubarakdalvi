# bigger string using one input and for loop and l just and rjust and center metnod
'''
word = 'H'
width = int(input('Enter Number : '))

for i in range(width):
    print((word * i).rjust(width - 1) + word * (i + 1))

for i in range(width+1):
    print((word * width).center(width * 2) +
          (word * width).center(width * 6))

for i in range((width + 1)//2):
    print((word * width * 5).center(width * 6))

for i in range(width + 1):
    print((word * width).center(width * 2) +
          (word * width).center(width * 6))
for i in range(width):
    print(((word * (width - i - 1)).rjust(width) + word +
          (word * (width - i - 1)).ljust(width)).rjust(width * 6))
'''
import decimal
import random
import string
import time

# using lst comprehension and \n we did this job
'''
def wrap(s,w):
    s = str(s)
    w = int(w)
    return '\n'.join(s[i:i+w] for i in range(0,len(s),w))

s = input('Enter String : ')
w = int(input('Enter Number : '))
print(wrap(s,w))
'''
'''
import timeit
def welcom():
    n,m = map(int,input('Enter NUmber : ').split())
    w = 'WELCOME'

    for i in range(1,n,2):
        print(('.|.' * i).center(m,'-'))

    print(w.center(m,'-'))

    for i in range(n-2,-1,-2):
        print(('.|.' * i).center(m,'-'))




start_time = timeit.default_timer()
welcom()
end_time = timeit.default_timer()
print(end_time - start_time)
'''
'''
def print_formatted(n):
    width = len(bin(n)) - 2
    for i in range(1,n+1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i,width=width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
'''

#not my logic
'''
def print_rangoli(size):
    for i in range(size):
        s = '-'.join(chr(ord('a')+size-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(size * 4 - 3,'-'))
    for i in range(size - 1):
        s = '-'.join(chr(ord('a')+ size - j - 1) for j in range(size-i-1))
        print((s+s[::-1][1:]).center(size * 4 - 3,'-'))

if __name__ == '__main__':
    size = int(input())
    print_rangoli(size)
'''


'''
#not my solution
import os

def solve(s):
    s = str(s)
    return ' '.join(s.capitalize() for s in s.split(' '))


output_path = os.path.realpath(__file__)
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result + '\n')
'''
'''
#thora bahot mera nyan
import string

def minion_game(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    alpha = string.ascii_uppercase
    consonants = [char for char in alpha if char not in vowels]
    stuart_word = ' '.join(consonants)
    kevin_word = ' '.join(vowels)
    stuart = 0
    kevin = 0

    for char in range(len(s)):
        if s[char] in stuart_word:
            stuart += len(s) - char
        elif s[char] in kevin_word:
            kevin += len(s) - char
    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif stuart < kevin:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
'''

