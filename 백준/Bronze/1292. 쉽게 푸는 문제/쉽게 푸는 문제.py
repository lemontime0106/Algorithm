A, B = map(int, input().split())

arr = []

num = 1
while len(arr) < B:
    for _ in range(num):
        arr.append(num)
    num += 1

print(sum(arr[A-1:B]))