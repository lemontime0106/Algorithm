N = int(input())
target = list(input())
answer = 0

for _ in range(N-1):
    temp = target[:]
    word = input()
    cnt = 0

    for w in word:
        if w in temp:
            temp.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(temp) < 2:
        answer += 1

print(answer)