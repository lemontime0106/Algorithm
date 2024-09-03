N = int(input())
A = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

A = set(A)

for i in lst:
    if i in A:
        print(1)
    else:
        print(0)