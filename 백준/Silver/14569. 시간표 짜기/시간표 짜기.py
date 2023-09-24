N = int(input())
subject = []
for i in range(N):
    lst = list(map(int, input().split()))
    a, time = lst[0], lst[1:]
    subject.append(time)

S = int(input())
for i in range(S):
    cnt = 0
    lst = list(map(int, input().split()))
    a, time = lst[0], lst[1:]
    schedule = [True] * 51
    for j in time:
        schedule[j] = False

    flag = False
    for j in subject:
        if not flag:
            temp = schedule[:]
        flag = True
        for k in j:
            if temp[k]:
                flag = False
                break
        if flag:
            cnt += 1


    print(cnt)

