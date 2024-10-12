for _ in range(int(input())):
    N, K, T, M = map(int, input().split())
    scores = {i: [0] * (K + 1) for i in range(1, N + 1)}
    cnt = [0] * (N+1)
    order = [0] * (N+1)

    for i in range(M):
        a, b, c = map(int, input().split())
        scores[a][b] = max(scores[a][b], c)
        cnt[a] += 1
        order[a] = i

    answer = sorted(scores, key=lambda x:[-sum(scores[x]), cnt[x], order[x]]).index(T) + 1

    print(answer)