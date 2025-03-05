import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if not x % i:
            return False
    return True

N = int(input())
answer = 0

for i in range(N, 1000001):
    if i == 1:
        continue

    if str(i) == str(i)[::-1]:
        if isPrime(i):
            answer = i
            break

if not answer:
    answer = 1003001

print(answer)