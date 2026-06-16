def solution(keymap, targets):
    answer = []

    temp = dict()

    for i in range(len(keymap)):
        word = keymap[i]

        for j in range(len(word)):
            if word[j] in temp:
                temp[word[j]] = min(temp[word[j]], j + 1)
            else:
                temp[word[j]] = j + 1

    for i in range(len(targets)):
        target = targets[i]
        cnt = 0

        for t in target:
            if t in temp:
                cnt += temp[t]
            else:
                cnt = -1
                break

        answer.append(cnt)

    return answer