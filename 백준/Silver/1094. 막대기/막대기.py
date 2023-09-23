X = int(input())
X_bin = bin(X)
ans = 0
for i in X_bin[1:]:
    if i == '1':
        ans += 1
print(ans)
