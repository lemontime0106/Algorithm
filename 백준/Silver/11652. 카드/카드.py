N = int(input())
card_dict = {}

for _ in range(N):
    i = int(input())
    if i not in card_dict:
        card_dict[i] = 1
    else:
        card_dict[i] += 1

most_frequent_item = sorted(card_dict.items(), key=lambda x: (-x[1], x[0]))[0][0]

print(most_frequent_item)
