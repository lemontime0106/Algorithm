def next(w):
    for i in range(len(w)-1, 0, -1):
        if w[i-1] < w[i]:
            for j in range(len(w)-1, i-1, -1):
                if w[i-1] < w[j]:
                    w[i-1], w[j] = w[j], w[i-1]
                    return (w[:i] + (w[i:][::-1]))
    return w

N = int(input())
for i in range(N):
    word = list(input())
    result = ''.join(next(word))
    print(result)