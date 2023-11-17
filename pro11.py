#created a class for user input and stored as key valu pair
import re
class Student:
    def __init__(self,name,id,email_id):
        self.name = name
        self.id = id
        self.email_id = email_id

        if not self.name.isalpha():
            print('Please Enter Valid Name')
        elif not self.id.isdigit():
            print('Please Enter Valid ID')
        elif not re.search('^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email_id):
            print('Please Enter Valid Email ')

try:
    all_students = {}
    num = int(input('Enter Number : '))
    n = 0
    while n < num:
        student1 = Student(input('Enter Name : '), input('Enter ID : '), input('Enter Email : '))
        all_students[student1.id] = student1
        n += 1
    for ir, student in all_students.items():
        print(f'ID : {ir} \n'
                f'Name: {student.name} \n'
                f'Email : {student.email_id} \n')
except Exception as e:
    print('Please Enter Valid Entry')
finally:
    print('Ahh That\'s The Programme Done')
