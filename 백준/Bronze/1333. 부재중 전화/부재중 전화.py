N, L, D = map(int, input().split())

t = 0

while True:
    can_hear = True

    for i in range(N):
        start = i * (L + 5)
        end = start + L

        if start <= t < end:
            can_hear = False
            break

    if can_hear:
        print(t)
        break

    t += D