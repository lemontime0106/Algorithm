N = int(input())
shortcut = set()

for _ in range(N):
    word = list(input().split())
    flag = False

    for i in range(len(word)):
        if word[i][0].upper() not in shortcut:
            shortcut.add(word[i][0].upper())
            flag = True
            word[i] = "[" + word[i][0] + "]" + word[i][1:]
            print(" ".join(word))
            break

    if not flag:
        for i in range(len(word)):
            check = False
            for j in range(len(word[i])):
                if word[i][j].upper() not in shortcut:
                    shortcut.add(word[i][j].upper())
                    flag = True
                    check = True
                    word[i] = word[i][:j] + "[" + word[i][j] + "]" + word[i][j+1:]
                    print(" ".join(word))
                    break
            if check:
                break
    if not flag:
        print(" ".join(word))