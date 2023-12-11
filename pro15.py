
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