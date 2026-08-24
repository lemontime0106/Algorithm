# 26942. 가전 설정 코드 풀기

hexa = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

for t in range(1, int(input())+1):
    N, code = input().split()

    N = int(N)

    answer = ""

    for i in code:
        if i in hexa:
            num = hexa[i]
        else:
            num = int(i)

        temp = ""

        for _ in range(4):
            temp = str(num % 2) + temp
            num //= 2

        answer += temp

    print(f"#{t} {answer}")

