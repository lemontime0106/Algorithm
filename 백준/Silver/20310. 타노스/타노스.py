N = list(input())

cnt = {0: 0, 1: 0}
for i in N:
    cnt[int(i)] += 1

remove_zero = cnt[0] // 2
remove_one = cnt[1] // 2

for _ in range(remove_zero):
    N = N[::-1]
    N.remove("0")
    N = N[::-1]

for _ in range(remove_one):
    N.remove("1")

print("".join(N))