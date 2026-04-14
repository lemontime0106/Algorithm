import sys

count = [0] * 26  # a~z

for line in sys.stdin:
    for ch in line:
        if 'a' <= ch <= 'z':
            count[ord(ch) - ord('a')] += 1

max_count = max(count)

result = []
for i in range(26):
    if count[i] == max_count:
        result.append(chr(i + ord('a')))

print(''.join(result))