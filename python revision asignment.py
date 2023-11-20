# factorial of function using recursion means function calling itself
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('Enter Number : '))
if n < 0:
    print('Sorry, Please Enter Positive integer')
else:
    print(f'The Factorial of {n} is {factorial(n)}')

# palindrome checker
def palindrome1(plndr):
    return plndr == plndr[::-1]
n = input('Enter To Check palindrome or not : ')
if palindrome1(n):
    print(n,'Is A Palindrome ')
else:
    print(n,'Is Not Palindrome')

# finding max element rom array of integers
# solution 1
n = input('Enter Number : ').split()
last1 = map(int,n)
print(f'the maximun number in the list is : {max(last1)}')

#solution 2
lst = []
n = input('Enter Number : ').split()
lst.append(n)
last1 = map(int,n)
print(f'the maximun number in the list is : {max(last1)}')

# count the number of words from sentence
lit = []
n = input('Enter Sentece : ').split()
lit.append(n)
print(len(lit[0]))

# fibonacci series
n = int(input('Enter Number : '))
fibo = [0, 1]
if n == 0:
    fibo = [0]
else:
    for i in range(2,n+1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
print(fibo)

# specifit number in fibanacci sereeies with recursive functon
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number: "))
print(f"The {n}th number in the Fibonacci sequence is {fibonacci(n)}")


# sum of list in the functions
def sum_of_list() -> None:
    n = input('Enter Number : ').split()
    lst = []
    for i in n:
        lst.append(n)
        n = list(map(int,n))
    print(sum(n))
sum_of_list()

# check number is prime or not
num = int(input('Enter Number To Check Whether It Is Prime Or Not : '))
if num == 0 or num == 1:
    print(False)
for i in range(2,num):
    if num % i == 0:
        print(False)
        break
else:
    print(True)

# alternate option

# check number is prime or not
n = int(input('Enter The Number To Check Prime Or Not : '))
if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            print(False)
            break
    else:
        print(True)
else:
    print(False)

#another eg

n = int(input('Enter Number :'))
for i in range(1,n+1):
    if n:
        print(i * '*')
else:
    print('THIS THE END')

# another for else eg

n = int(input('Enter number : '))
for i in range(1,n+1):
    print(i)
    if i == 5:
        break
else:
    print('HEllO THERE')

#while else eg
i = int(input('Enter Number :'))
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# while if elif else
n = int(input('Enter Number : '))
while n <= 6:
    if n == 0:
        print('The Value Of n Is :',n)
        n += 1
    elif n == 1:
        print('The Value Of n Is :',n)
    elif n == 2:
        print('The Value Of n Is :',n)
        n +=1
    elif n == 3:
        print('The Value Of n Is :',n)
        n +=1
    elif n == 4:
        print('The Value Of n Is :',n)
        n += 1
    else:
        print('The Value Of n Is :',n)
        n += 1

# int list sorting via bubble sort algorithm
def my_method(number):
    n = len(number)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if number[j] > number[j+1]:
                number[j],number[j+1] = number[j+1],number[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == '__main__':
    number = list(map(int,input('Enter Number In the List : ').split()))
    my_method(number)
    number = number[::-1]
    for i in range(len(number)):
        print('%d' % number[i],end=' ')

# decimal to binary
def dec_bin(number):
    whole, dec = str(number).split('.')
    whole = int(whole)
    dec = int(dec)
    res = bin(whole).lstrip('0b') + '.'
    for _ in range(3):
        whole, dec = str((decimal_converter(dec)) * 2).split('.')
        dec = int(dec)
        res += whole
    return res
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

n = float(input('Enter NUmber : '))
print(dec_bin(n))

#shukar

import math
def circle(r):
    pi = math.pi
    radius = r
    area_of_circle = pi * (radius ** 2)
    return area_of_circle
if __name__ == '__main__':
    calulate_circle = int(input('Enter Radius TO Find The Area : '))
    print(circle(calulate_circle))

# count of vowels

vowel = ['a','e','i','o','u']
usr_inp = input('Enter Sentence To Check : ')
cnt = sum(usr_inp.lower().count(vowels) for vowels in vowel)
print(cnt)

# second largest nunber
def second_largest(*args):
    uni_num = list(set(args))
    uni_num.sort()
    if len(uni_num) < 2:
        return None
    return uni_num[-2]

args= list(map(int,input("Enter Numbers : ").split()))
print(second_largest(*args))

# reverse the string

def reverse_string(wrd:str):
    lst = list(wrd)
    lst = lst[::-1]
    return ''.join(lst)

word = input('Enter Word To Reversed It : ')
print(reverse_string(word))

#check for perfect square

def perfect_square(n):
    ps = int(n ** 0.5)
    if ps ** 2 == n:
        return True
    else:
        return False

usr_inp = int(input('Enter Number : '))
print(perfect_square(usr_inp))

# common element searching
def common_element(*args):
    sets = [set(lst) for lst in args]
    common = set.intersection(*sets)
    return list(common)

usr_inp = input('Enter Usr Inp Seperated Each Word By Comma : ').split(',')
matched_elmt = input("Enter Matched Element To Check In Usr Inp Separated By Comma : ").split(',')

common = common_element(usr_inp,matched_elmt)

if common:
    print(f'Common Element Were In The List Are : {common}')
else:
    print(f'No Common Element Was Found During Checking ')

#leap year
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

usr_input = int(input('Enter Year To Check It Is Leap Year Or Not : '))

if leap_year(usr_input):
    print('It\'s A Leap Year')
else:
    print('It\'s Not A Leap Year')


# factorial is iterating over provided input and giving output

def iter_fact(num):
    lst = 1
    for i in range(1,num+1):
        lst *= i
    return  lst


number = int(input('Enter Number To Get Iter Fact : '))
print(iter_fact(number))

#maximum_occurence in list
def maximum_occurence(word):
    lst = {}
    for i in word:
        if i in lst:
            lst[i] += 1
        else:
            lst[i] = 1
    return max(lst,key=lst.get)

wrd = input('Enter To Get Maximum Occurence Count : ')
print(maximum_occurence(wrd))

# random password generator

import re
def rand_pass(passwrd):
    if re.match('[ ]',passwrd):
        return 'Please Provide Password'
    if len(passwrd) <= 7:
        return 'Weak Password '
    elif len(passwrd) >= 20:
        return 'Haha Too long Password You Wanna Write Essay Or Something '
    elif re.match('[*+=/()&6%$#@!~]]{0}',passwrd):
        return 'Please Dont Create The Pass WORD Starts With These : *+=/()&6%$#@!~'
    elif re.search('[A-Z]{0}',passwrd) or re.search('[a-z]',passwrd) and re.search('[0-9]',passwrd) or re.search('[*+=/()&6%$#@!~]',passwrd):
        return 'You Have Generated ThE BesT Password For Yout System'
    elif re.search('[A_Z]',passwrd) or re.search('[0-9]',passwrd) and re.search('[*+=/()&6%$#@!~]',passwrd):
        return 'You\'ve Got SOMETHING DIFFERENT'
validate_password = input('Enter Password To Validate : ')
print(rand_pass(validate_password))

#another method

import random
import string
def password_generator(passwrd):
    letters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation


    password = [random.choice(letters),random.choice(numbers),random.choice(punctuation)]


    for _ in range(passwrd - 3):
        password.append(random.choice(letters+punctuation+numbers))

    random.shuffle(password)

    password = ''.join(password)
    return password
prd = int(input('Enter Lenght Of Pass To Generate It : '))
password = password_generator(prd)
if len(password) < 7:
    print('Please Enter Strong Password')
elif len(password) >= 20:
    print('Your Password Is To Long ')
else:
    print(f'SuccessFully Generated A New Password, That Is : {password}')
