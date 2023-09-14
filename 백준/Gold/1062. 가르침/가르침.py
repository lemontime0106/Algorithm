import sys

base_char = ['a', 'n', 't', 'i', 'c']


def dfs(cnt, start, stack, lst, v):
    if cnt == possible:
        combination.append(stack[:])
        return

    for i in range(start, len(lst)):
        if not v[i]:
            v[i] = True
            stack.append(lst[i])
            dfs(cnt + 1, i + 1, stack, lst, v)
            stack.pop()
            v[i] = False


N, K = map(int, sys.stdin.readline().split())
flag = True

if K <= 4:
    flag = False

if flag:
    word = []
    possible = K - 5
    for _ in range(N):
        word.append(set(sys.stdin.readline().strip()))
    char_lst = set()
    char = [[] for _ in range(N)]

    for i in range(len(word)):
        for j in word[i]:
            if j not in base_char:
                char[i].append(j)
                char_lst.add(j)
    
    if len(char_lst) <= possible:
        print(N)
        exit(0)

    combination = []
    visited = [False] * len(char_lst)
    dfs(0, 0, [], list(char_lst), visited)

    max_count = 0
    for k in range(len(combination)):
        cnt = 0
        if max_count == N:
            break

        for i in range(len(char)):
            temp = 0
            for j in range(len(char[i])):
                if char[i][j] in combination[k]:
                    temp += 1
            if temp == len(char[i]):
                cnt += 1
        max_count = max(max_count, cnt)
    print(max_count)

else:
    print(0)