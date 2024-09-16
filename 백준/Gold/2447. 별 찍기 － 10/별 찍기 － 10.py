N = int(input())

def solution(n):
    if n == 3:
        return ["***", "* *", "***"]

    pervious = solution(n//3)
    stars = []

    for i in range(3):
        for line in pervious:
            if i == 1:
                stars.append(line + " " * (n//3) + line)
            else:
                stars.append(line * 3)

    return stars

answer = solution(N)
for i in answer:
    print(i)