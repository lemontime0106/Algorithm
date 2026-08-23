# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호

for t in range(1, 11):
    N, nums = map(str, input().split())
    N = int(N)

    answer = ""

    for i in nums:
        if len(answer) == 0:
            answer += i

        else:
            if answer[-1] == i:
                answer = answer[:-1]

            else:
                answer += i

    print(f"#{t} {answer}")