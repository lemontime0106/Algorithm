n = input().strip()

for i in range(1, len(n)):
    left = 1
    right = 1

    for ch in n[:i]:
        left *= int(ch)

    for ch in n[i:]:
        right *= int(ch)

    if left == right:
        print("YES")
        break
else:
    print("NO")