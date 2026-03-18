def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(input())

for _ in range(T):
    lst = list(map(int, input().split()))
    N = lst[0]
    nums = lst[1:]

    answer = 0

    for i in range(N):
        for j in range(i+1, N):
            answer += gcd(nums[i], nums[j])

    print(answer)
