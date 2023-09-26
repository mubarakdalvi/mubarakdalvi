input1 = map(int,input('Enter Number to check Weather Odd or Even : ').split())
for i in input1:
    if i % 2 == 0:
        print(f'"{i} is Even"')
    elif i % 2 != 0:
        print(f'"{i} is Odd"')