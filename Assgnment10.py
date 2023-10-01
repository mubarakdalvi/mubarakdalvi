# Indexing Lists:
# Given a list numbers = [1, 2, 3, 4, 5], write Python code to print the third element of the list.
list1 = [1, 2, 3, 4, 5]
print(list1[2])

"""
Selection with Conditional Statements:
Write a Python program that takes an integer as input and prints "Even" if it's even and "Odd"
if it's odd.
"""

input1 = int(input('Enter Number To Check whether its Even Or Odd :'))
if input1 % 2 == 0:
    print('Even')
elif input1 %2 == 1:
    print('Odd')

# code for nested list and finding a element by index searching
list1 = [[0,0],[0,1],[1,0],[1,1],[0,2],[2,0]]
fr_sc = list1[2]
print('The second row and first column element is ',fr_sc)

# code for find print last word of the string
string = 'Hello, World!'
print(string[12])

# code for printing 2 to 4 position element in list
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])

# Create a dictionary representing a person's information (name, age, city). Write code to print
# only the person's age
persons_information = {
    'name': 'person_name',
    'age': 40,
    'city': 'person_city'
}
print(persons_information['age'])

'''Nested Dictionaries:
Create a nested dictionary representing a library catalog. Write code to access the title of a
book with a specific ISBN number.
'''

library_catalog = {
    '978-3-16-148410-0': {
         'Book_Title' : 'Tiger', 'library-location or book_location' : 'Pune'},
    '975-3-56-178410-0': {
        'Book_Title': 'Ocean', 'library-location or book_location': 'Mumbai'},
    '752-1-56-538489-1': {
        'Book_Title': 'Space', 'library-location or book_location': 'Bengaluru'}
}

print(library_catalog['752-1-56-538489-1']['Book_Title'])


'''
Tuple Indexing:
Given a tuple my_tuple = (10, 20, 30, 40, 50), write Python code to print the third element.
'''

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[2])

'''
List Comprehension:
Generate a list of even numbers from 1 to 20 using list comprehension.
'''

print([x for x in range(1,21) if x % 2 == 0])

'''
Accessing Nested Lists:
Create a nested list containing student names and their exam scores. Write code to print the
score of a specific student.
'''

student_Name = [{'amit': 41}, {'shubham': 40}, {'kity': 42}]

def student_score():
    a = input('Enter student Name To Get Score : ')
    for student in student_Name:
        if a in student:
            return student[a]
    return 'No Student Of That Name Found'
print(student_score())

# Use Case: Email Address Validation
# Create a Python program to validate email addresses using regular expressions. Email
# validation is a common task in applications to ensure that user-provided email addresses are in
# the correct format.

import re
def valid_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(pattern, email):
        return "Yes, Its a Valid Email Id"
    else:
        return "No, Please Enter Valid Email Id"
x = input('Enter email-id : ')
print(valid_email(x))
print('Thanks For Using This Programme')

'''
Use Case: Password Strength Checker
Create a Python program to check the strength of user-provided passwords using regular
expressions. Password strength is crucial for security, and this program will help users evaluate
the strength of their passwords.
'''


import re

import re

def password_checker(password):
    if len(password) <= 7 < 17:
        return 'Weak "Password" HAHA Noob '
    if re.match('[-%$^*()+=_#@!]]{0}',password):
        return 'Please Do Not Create Password From These "-%$^*()+=_#@!" Characters '
    if re.search('[A-Z]', password) and re.search('[a-z]', password) and re.search('[0-9]',password) and re.search('[.*&^%$;#:@+=-_!()]',password):
        return 'Strong "Password" Yeah Pro Bro'
    if re.search('[A-Z]*',password) and re.search('[0-9]',password) and re.search('[-%$^*()+=_#@!]', password):
        return 'Ahh You Got Something Different'
validate = input('Enter Password To Check Its Weak or Strong or unique : ')
print(password_checker(validate))