'''
this is the link of https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true of the challenge it is easy but i am not able to solve
this i got help from gpt but vant understand where to use for loop, whlile loop , have idea of if else in there are many examples where i was stuck at loops
and where to use them. and i was using inex but have to provided hard coded sting in it.
'''
from collections import Counter,defaultdict # inported Counter And default dict

# giving a range to list
n, m = map(int,input('Enter range of the list separated by space : ').split())
print(f'Enter {n} words for Group A:')
A = [input() for _ in range(n)]
print(f'Enter {m} words for Group B:')
B = [input() for _ in range(m)]

dict1 = defaultdict(list)
for i, word in enumerate(A, start=1):
    dict1[word].append(i)

for word in B:
    if word in dict1:
        print(' '.join(map(str, dict1[word])))
    else:
        print(-1)
 # i am getting error here

'''
also i had tried
if A is in B:
    print(A.index(hard coded)
else:
    print(B.index(hard coded)
'''

'''
i want get this result
5 2
a
a
b
a
b
a
b
1 2 4
3 5
'''