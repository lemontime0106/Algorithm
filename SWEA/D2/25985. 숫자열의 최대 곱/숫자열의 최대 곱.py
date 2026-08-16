# 25985. 숫자열의 최대 곱

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = -float("inf")

    for i in range(-(M-1), N):
        temp = 0

        for j in range(M):
            a_idx = i + j

            if 0 <= a_idx < N:
                temp += A[a_idx] * B[j]

        answer = max(answer, temp)

    print(f"#{t} {answer}")