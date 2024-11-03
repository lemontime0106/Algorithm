from collections import defaultdict

def count_cnt(word, cnt):
    short, long = float("inf"), -1
    count = defaultdict(list)

    for i in range(len(word)):
        count[word[i]].append(i)

    for idx_list in count.values():
        if len(idx_list) < cnt:
            continue

        for i in range(len(idx_list)-cnt+1):
            short = min(short, idx_list[i+cnt-1] - idx_list[i] + 1)
            long = max(long, idx_list[i+cnt-1] - idx_list[i] + 1)
    return short, long

for _ in range(int(input())):
    W = list(input().strip())
    K = int(input().strip())

    answer_short, answer_long = count_cnt(W, K)

    if answer_long != -1:
        print(answer_short, answer_long)
    else:
        print(-1)
