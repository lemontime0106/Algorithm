lst = list(map(int, input().split()))

temp = 0

for i in lst:
    temp += i ** 2

print(temp % 10)