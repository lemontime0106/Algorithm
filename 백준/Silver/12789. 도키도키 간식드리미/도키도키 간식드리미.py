import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
target = 1

for num in arr:
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

    if num == target:
        target += 1
    else:
        stack.append(num)

while stack and stack[-1] == target:
    stack.pop()
    target += 1

print("Nice" if target == N + 1 else "Sad")