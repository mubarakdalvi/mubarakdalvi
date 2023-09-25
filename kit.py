# code for rectangle area
l , b = map(float,input().split())
area = l * b
print(int(area))

# code for display name and age
a = input('Enter Name : ')
b = int(input('Enter Number : '))
print('The Name of the person is:',a,'and his age is :', b)

#code for swapping
def swapNumber(a:list,  b: list) -> None:
    print('The output of the above test case is',b,a)
swapNumber(5, 4)


# code for average of student
dic = {}
for n in range(int(input('student '))):
    name, *marks = input('name ').split()
    marks = list(map(float, marks))
    dic[name] = marks
query_name = input('query ')
if query_name in dic:
    print(sum(dic[query_name]) / len((dic[query_name])))
else:
    print('There is not student name like this')
