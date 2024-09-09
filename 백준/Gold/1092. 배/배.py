N = int(input())
weight = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

weight.sort(reverse=True)
box.sort(reverse=True)

if max(weight) < max(box):
    print(-1)
else:
    answer = 0
    while box:
        i = 0
        j = 0
        while i < len(weight) and j < len(box):
            if weight[i] >= box[j]:
                box.pop(j)
                i += 1
            else:
                j += 1
        answer += 1

    print(answer)