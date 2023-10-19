N = int(input())
stack = set()
ans = 0
cnt = 0
for _ in range(N):
    temp = input()
    if temp == 'ENTER':
        ans += cnt
        cnt = 0
        stack.clear()
    else:
        if temp not in stack:
            cnt += 1
            stack.add(temp)
ans += cnt
print(ans)