N = int(input())

answer = 1

while N > 0:
    answer *= N
    N -= 1

print(answer)