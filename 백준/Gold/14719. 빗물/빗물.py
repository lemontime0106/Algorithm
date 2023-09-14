H, W = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
H_idx = lst.index(max(lst)) # 최대높이

# 왼쪽 > 오른쪽
cur_h = lst[0]
for i in range(1, H_idx):
    if cur_h > lst[i]:
        cnt += cur_h - lst[i]

    else:
        cur_h = lst[i]

cur_h = lst[-1]
for i in range(W-2, H_idx-1, -1):
    if cur_h > lst[i]:
        cnt += cur_h - lst[i]
    else:
        cur_h = lst[i]

print(cnt)