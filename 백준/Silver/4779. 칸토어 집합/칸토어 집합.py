def solution(n):
    if n == 1:
        return "-"
    else:
        left = solution(n // 3)
        center = " " * (n // 3)
        return left + center + left

while True:
    try:
        N = int(input())
        answer = solution(3 ** N)
        print(answer)
    except:
        break

