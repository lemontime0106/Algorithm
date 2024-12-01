N = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = lst[-1]
for i in range(N-1):
    answer += lst[i] / 2

print(answer)