import math

N = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def dfs(number, cnt, n):
    if cnt == n:
        print(number)
        return

    for i in range(1, 10, 2):
        next_number = number * 10 + i
        if is_prime(next_number):
            dfs(next_number, cnt + 1, n)

def solution(n):
    initial_prime = [2, 3, 5, 7]
    for i in initial_prime:
        dfs(i, 1, N)

solution(N)