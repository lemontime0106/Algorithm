N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for i in lst:
    student = i

    student -= B
    answer += 1

    if student > 0:
        answer += (student // C)
        if student % C != 0:
            answer += 1

print(answer)
