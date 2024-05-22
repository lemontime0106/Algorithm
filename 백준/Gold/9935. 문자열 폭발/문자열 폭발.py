S = list(input())
boom = input()

lst = []
B = len(list(boom))

for i in range(len(S)):
    lst.append(S[i])
    if lst[-B:] == list(boom):
        for _ in range(B):
            lst.pop()

if lst:
    print(''.join(lst))
else:
    print("FRULA")