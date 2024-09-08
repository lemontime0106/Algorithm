L, R = map(int, input().split())

strL, strR = str(L), str(R)

if len(strL) != len(strR):
    print(0)

else:
    min_cnt = 0
    for i in range(len(strL)):
        if strL[i] != strR[i]:
            break
        if strL[i] == "8":
            min_cnt += 1

    print(min_cnt)