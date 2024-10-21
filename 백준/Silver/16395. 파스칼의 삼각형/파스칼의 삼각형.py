N, K = map(int, input().split())

pascal = [[1] * (i+1) for i in range(N)]

for i in range(2, N):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

print(pascal[N-1][K-1])