'''
The asterisk * before b in pow(a, *b) is used for unpacking the list b.
In Python, the * operator is used in function calls to unpack an iterable into the arguments in the function call.
When we write *b, it means “use the elements of b as separate arguments to this function”.
So, if b is a list of one element, like [2], pow(a, *b) is equivalent to pow(a, 2).
If b is an empty list [], pow(a, *b) is equivalent to pow(a).
This is a very powerful feature in Python that allows for more flexible function calls. 😊
'''
import math

'''
a,*b = map(int,input('Enter Number : ').split())
print(pow(a,*b))
'''
'''new '''
import math
a = int(input('Enter Number a: '))
b = int(input('Enter Number b: '))
m = int(input('Enter Number m: '))
print(int(math.pow(a,b)))
print(pow(a, b, m))
