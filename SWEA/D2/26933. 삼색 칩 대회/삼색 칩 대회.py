
def fight(a, b):
    if cards[a] == cards[b]:
        return min(a, b)

    if (cards[a] == 1 and cards[b] == 3) or \
       (cards[a] == 2 and cards[b] == 1) or \
       (cards[a] == 3 and cards[b] == 2):
        return a

    return b


def winner(start, end):
    if start == end:
        return start

    mid = (start + end) // 2

    left = winner(start, mid)
    right = winner(mid + 1, end)

    return fight(left, right)


for t in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    answer = winner(0, N - 1)

    print(f"#{t} {answer + 1}")