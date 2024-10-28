X = int(input())
N = int(input())
sum = 0
for i in range(N):
  price, cnt = map(int, input().split())
  sum += (price*cnt)

if X == sum:
  print("Yes")
else:
  print("No")