N, T = map(int, input().split())

L = list(map(int, input().split()))
R = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
lst = [*L, *R, *D]

for _ in range(T):
    temp = lst.pop()
    lst.insert(0, temp)

for i in range(0, N*3, N):
    print(*lst[i:i+N])