G = int(input())

left, right = 1, 2

answer = []

while True:
    if right ** 2 - (right-1) ** 2 > 100000:
        break

    if right ** 2 - left  ** 2 < G:
        right += 1
    elif right  ** 2 - left  ** 2 > G:
        left += 1
    elif right  ** 2 - left  ** 2 == G:
        answer.append(right)
        right += 1

if answer:
    for a in answer:
        print(a)
else:
    print(-1)