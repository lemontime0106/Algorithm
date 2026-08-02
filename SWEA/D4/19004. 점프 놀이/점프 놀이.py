for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())

    # positions[x] = 숫자 x가 적힌 타일들의 좌표
    positions = [[] for _ in range(K + 1)]

    for y in range(N):
        row = list(map(int, input().split()))

        for x in range(N):
            positions[row[x]].append((y, x))

    # 1 ~ K 중 하나라도 존재하지 않는다면 게임 자체가 불가능
    possible = True

    for number in range(1, K + 1):
        if not positions[number]:
            possible = False
            break

    if not possible:
        print(f"#{t} -1")
        continue

    # 숫자 1은 어느 곳에서 시작해도 되므로 비용은 모두 0
    prev_positions = positions[1]
    prev_cost = [0] * len(prev_positions)

    # 2 -> 3 -> ... -> K 순서로 진행
    for number in range(2, K + 1):

        current_positions = positions[number]
        current_cost = []

        # 현재 number가 적힌 각각의 타일에 대해서
        for y, x in current_positions:

            min_cost = float("inf")

            # 이전 숫자 number-1이 적힌 모든 타일을 확인
            for i in range(len(prev_positions)):
                py, px = prev_positions[i]

                # 이전 위치까지 오는데 걸린 거리
                # +
                # 이전 위치 -> 현재 위치 점프 거리
                distance = (
                    prev_cost[i]
                    + abs(y - py)
                    + abs(x - px)
                )

                min_cost = min(min_cost, distance)

            current_cost.append(min_cost)

        # 다음 숫자를 위해 현재 결과를 이전 결과로 변경
        prev_positions = current_positions
        prev_cost = current_cost

    # K가 적힌 타일들 중 최소 비용
    answer = min(prev_cost)

    print(f"#{t} {answer}")