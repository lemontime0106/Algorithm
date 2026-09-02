# 1945. 간단한 소인수분해

for t in range(1, int(input()) + 1):
    N = int(input())

    nums = [2, 3, 5, 7, 11]
    answer = [0] * 5

    for i in range(5):
        while N % nums[i] == 0:
            answer[i] += 1
            N //= nums[i]

    print(f"#{t}", *answer)