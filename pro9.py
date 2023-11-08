'''
a = int(input('Enter Number a : ')): This line asks the user to enter a number for variable a.
The int(input()) function reads the user’s input as a string, then converts it to an integer.
b = int(input('Enter Number b : ')): Similarly, this line asks the user to enter a number for variable b.
c = int(input('Enter Number c : ')): This line asks the user to enter a number for variable c.
d = int(input('Enter Number d : ')): This line asks the user to enter a number for variable d.
e = a**b + c**d: This line performs the calculation. It raises a to the power of b and c to the power of d,
then adds the two results together.
The ** operator in Python is used for exponentiation.
print(e): Finally, this line prints the result of the calculation.
The print() function in Python outputs the value of the variable or expression inside the parentheses to the console.
In this case, it prints the value of e, which is the result of the calculation.
So, if you run this script and enter 2 for a, 3 for b, 4 for c, and 5 for d,
the script will calculate 2**3 + 4**5 (which equals 8 + 1024), and print 1032.
'''
a = int(input('Enter NUmber a : '))
b = int(input('Enter NUmber b : '))
c = int(input('Enter NUmber c : '))
d = int(input('Enter NUmber d : '))
e = a**b + c**d
print(e)
