n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

a_lst.sort()
b_lst.sort(reverse=True)

sum_lst = []
sum_n = 0

for i in range(n):
    sum_n += a_lst[i] * b_lst[i]
sum_lst.append(sum_n)

ans = max(sum_lst)

print(ans)