H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]

for i in range(X, H):
    for j in range(Y, W):
        B[i][j] = B[i][j] - B[i-X][j-Y]

for i in B[:H]:
    print(*i[:W])