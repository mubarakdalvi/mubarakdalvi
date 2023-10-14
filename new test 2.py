T = int(input())
for _ in range(T):
    x = int(input())
    a = input().split()
    A = {int(num) for num in a}

    x = int(input())
    b = input().split()
    B = {int(num) for num in b}
    if A.issubset(B):
        print(True)
    else:
        print(False)







