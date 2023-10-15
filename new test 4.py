A = {int(num) for num in input().split()}

T = int(input())
for _ in range(T):
    n = {int(num) for num in input().split()}

if A.issuperset(n) and A != n:
    print(True)
else:
    print(False)

