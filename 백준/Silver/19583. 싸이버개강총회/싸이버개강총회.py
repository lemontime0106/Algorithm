S, E, Q = input().split()
S = int(S[:2] + S[3:])
E = int(E[:2] + E[3:])
Q = int(Q[:2] + Q[3:])

answer = set()
cnt = 0

while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= S:
            answer.add(name)
        elif E <= time <= Q and name in answer:
            answer.remove(name)
            cnt += 1
    except:
        break

print(cnt)