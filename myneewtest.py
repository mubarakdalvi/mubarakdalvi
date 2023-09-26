# two integera checkibg for even or odd

input1, input2 = map(int,input('Enter Number To Check whether its Even Or Odd : ').split())
list1 = [input1, input2]
for i in list1:
    if i % 2 == 0 and i % 2 == 0:
        print(f"{i} is Even", end = '|')
    elif i % 2 != 0 and i % 2 != 0:
        print(f"{i} is Odd", end = '|' )