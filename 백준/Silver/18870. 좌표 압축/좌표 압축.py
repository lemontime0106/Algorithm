N = int(input())

X = list(map(int, input().split()))

X_sort = sorted(list(set(X)))

dic = {}
for i in range(len(X_sort)):
  dic[X_sort[i]] = i

for i in X:
  print(dic[i], end=" ")