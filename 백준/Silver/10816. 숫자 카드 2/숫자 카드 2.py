N = int(input())
lst = list(map(int, input().split()))

M = int(input())
card = list(map(int, input().split()))

number_dict = {}
answer = []

for l in lst:
    if l not in number_dict:
        number_dict[l] = 1
    else:
        number_dict[l] += 1

for c in card:
    if c not in number_dict:
        answer.append(0)
    else:
        answer.append(number_dict[c])

print(*answer)