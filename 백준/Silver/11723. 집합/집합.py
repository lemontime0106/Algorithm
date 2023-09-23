import sys
input = sys.stdin.readline

N = int(input())
s = 0

for _ in range(N):
    lst = list(input().split())
    if lst[0] == 'add':
        s = s | (1 << int(lst[1]))
    elif lst[0] == 'remove':
        s = s & ~(1 << int(lst[1]))
    elif lst[0] == 'check':
        if s & (1 << int(lst[1])):
            print(1)
        else:
            print(0)
    elif lst[0] == 'toggle':
        s = s ^ (1 << int(lst[1]))
    elif lst[0] == 'all':
        s = (1 << 21) - 1
    elif lst[0] == 'empty':
        s = 0