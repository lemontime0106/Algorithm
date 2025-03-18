from collections import defaultdict

N = int(input())

dance = defaultdict(bool)
dance["ChongChong"] = True
answer = 1

for _ in range(N):
    a, b = map(str, input().split())

    if dance[a]:
        if not dance[b]:
            dance[b] = True
            answer += 1

    elif dance[b]:
        dance[a] = True
        answer += 1

print(answer)