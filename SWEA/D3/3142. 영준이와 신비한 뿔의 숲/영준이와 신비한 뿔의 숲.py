for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    twin = n - m
    unicorn = 2*m-n

    print(f"#{tc} {unicorn} {twin}")