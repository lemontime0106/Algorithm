nums = list(map(int, input().split()))

def find_num(lst):
    a = int("".join(map(str, lst)))
    for i in range(1, 4):
        temp = int("".join(map(str, lst[i:] + lst[:i])))

        if a > temp:
            a = temp
    return a

answer = find_num(nums)
cnt = 1

for i in range(1111, answer):
    if "0" not in list(str(i)) and i == find_num(list(map(int, str(i)))):
        cnt += 1

print(cnt)
