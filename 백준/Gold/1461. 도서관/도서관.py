N, M = map(int, input().split())
books = list(map(int, input().split()))

positive = []
negative = []
last = 0

for book in books:
    last = max(abs(book), last)
    if book > 0:
        positive.append(book)
    else:
        negative.append(-book)

positive.sort(reverse=True)
negative.sort(reverse=True)
answer = 0

for i in range(0, len(positive), M):
    answer += positive[i] * 2
for i in range(0, len(negative), M):
    answer += negative[i] * 2

print(answer-last)