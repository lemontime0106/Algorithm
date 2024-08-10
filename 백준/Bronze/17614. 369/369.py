N = int(input())

game = {}

for i in range(1, N+1):
    for j in str(i):
        if int(j) not in game:
            game[int(j)] = 1
        else:
            game[int(j)] += 1

answer = game[3] + game[6] + game[9]

print(answer)