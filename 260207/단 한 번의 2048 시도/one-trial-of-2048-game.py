def process(line):
    # 1. 0 제거
    nums = [x for x in line if x != 0]

    merged = []
    i = len(nums) - 1
    while i >= 0:
        if i > 0 and nums[i] == nums[i-1]:
            merged.append(nums[i] * 2)
            i -= 2
        else:
            merged.append(nums[i])
            i -= 1

    merged.reverse()
    return [0] * (4 - len(merged)) + merged

MAP = [list(map(int, input().split())) for _ in range(4)]
D = input()

new = [[0]*4 for _ in range(4)]

for i in range(4):
    if D in ('L', 'R'):
        line = MAP[i][:]
        if D == 'L':
            line.reverse()

        result = process(line)

        if D == 'L':
            result.reverse()

        new[i] = result

    else:  # U, D
        line = [MAP[j][i] for j in range(4)]
        if D == 'U':
            line.reverse()

        result = process(line)

        if D == 'U':
            result.reverse()

        for j in range(4):
            new[j][i] = result[j]

for row in new:
    print(*row)
