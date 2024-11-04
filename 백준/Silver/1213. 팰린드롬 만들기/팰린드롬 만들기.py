from collections import Counter

word = input()
counter = Counter(word)

cnt = 0
answer = ""
start, mid = "", ""

for a, b in list(counter.items()):
    if b % 2 == 1:
        cnt += 1
        mid = a
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit(0)

for a, b in sorted(counter.items()):
    start += (a * (b // 2))
print(start + mid + start[::-1])