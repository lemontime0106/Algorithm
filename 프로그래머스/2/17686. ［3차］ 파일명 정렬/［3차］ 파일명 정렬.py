def solution(files):
    answer = []

    for file in files:
        head, number, tail = "", "", ""

        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                break

        answer.append([head, number, tail])

    answer = sorted(answer, key=lambda x: (x[0].upper(), int(x[1])))

    return ["".join(i) for i in answer]