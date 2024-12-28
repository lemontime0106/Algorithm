from collections import defaultdict

N = int(input())

cnt = defaultdict(int)

for _ in range(N):
    book_title = input()
    cnt[book_title] += 1

result = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])