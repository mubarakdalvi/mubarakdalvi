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