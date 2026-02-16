N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

segments.sort(key=lambda x: x[1])

count = 0
last_end = -float('inf')

for start, end in segments:
    if start > last_end:
        count += 1
        last_end = end

print(count)
