N, T = map(int, input().split())
U = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
lst = [*U, *D]

for _ in range(T):
    temp = lst.pop()
    lst.insert(0, temp)

print(*lst[:N])
print(*lst[N:])