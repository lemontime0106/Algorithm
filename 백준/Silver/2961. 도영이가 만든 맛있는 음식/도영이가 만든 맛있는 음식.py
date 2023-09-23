import sys
# input = sys.stdin.readline

N = int(input())
arr = []
comb = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

ans = float('inf')
for i in range(1<<N):
    S, B = 1, 0
    for j in range(N):
        if i & (1 << j):
            S *= arr[j][0]
            B += arr[j][1]
    if i:
        ans = min(ans, abs(S-B))

print(ans)