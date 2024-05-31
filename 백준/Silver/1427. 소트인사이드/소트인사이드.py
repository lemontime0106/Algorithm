N = list(map(int, input()))

N.sort(reverse=True)

answer = "".join(map(str, N))

print(answer)
