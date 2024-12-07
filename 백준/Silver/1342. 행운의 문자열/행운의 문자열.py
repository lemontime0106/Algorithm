word = input()

answer = set()
visited = [False] * len(word)

def backtracking(w):
    if len(w) == len(word):
        answer.add(w)
        return

    for i in range(len(word)):
        if not visited[i] and (not w or w[-1] != word[i]):
            visited[i] = True
            backtracking(w + word[i])
            visited[i] = False

backtracking("")
print(len(answer))