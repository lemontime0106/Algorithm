import math

D, H, W = map(int, input().split())

k = D / math.sqrt(H * H + W * W)
height = int(H*k)
width = int(W*k)

print(height, width)