L, C = map(int, input().split())
lst = list(input().split())

lst.sort()

comb = []
def dfs(start, stack):
    if len(stack) == L:
        comb.append(stack[:])
        return

    for k in range(start, C):
        stack.append(lst[k])
        dfs(k + 1, stack)
        stack.pop()

dfs(0, [])

answer = []

def is_valid(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_cnt = sum(1 for char in password if char in vowels)
    consonant_cnt = len(password) - vowel_cnt
    return vowel_cnt >= 1 and consonant_cnt >= 2

for c in comb:
    if is_valid(c):
        answer.append(c)

for a in answer:
    print("".join(a))