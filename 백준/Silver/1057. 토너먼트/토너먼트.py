N, A, B = map(int, input().split())
answer = 0

while A != B:
    A -= A // 2
    B -= B // 2
    answer += 1

print(answer)