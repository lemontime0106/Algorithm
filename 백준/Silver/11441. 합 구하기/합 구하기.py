N = int(input())
lst = list(map(int, input().split()))
M = int(input())
p_lst = [lst[0]] + [0] * (N-1)

for i in range(1, N):
    p_lst[i] = p_lst[i-1] + lst[i]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1

    if a == 0:
        print(p_lst[b])
    else:
        print(p_lst[b] - p_lst[a-1])
