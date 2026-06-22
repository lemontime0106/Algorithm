def solution(n):
    temp = ""

    while n > 0:
        temp += str(n % 3)
        n //= 3

    answer = 0

    for i in range(len(temp)):
        answer += int(temp[i]) * (3 ** (len(temp) - i - 1))

    return answer