# 26927. 다트 최다 점수 집계

for t in range(1, int(input())+1):
    N = int(input())
    score = input().strip()

    cnt = [0] * 10

    for s in score:
        cnt[int(s)] += 1

    max_cnt = max(cnt)
    answer = 0

    for i in range(10):
        if cnt[i] == max_cnt:
            answer = i

    print(f"#{t} {answer} {max_cnt}")

