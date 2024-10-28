def solution(n, info):
    answer = []
    ryan = [0] * 11
    max_diff = 0  # diff 변수를 max_diff로 명명하여 clarity를 높임

    def dfs(arrows, idx):
        nonlocal answer, max_diff  # 외부의 answer와 max_diff에 접근

        # 화살을 다 쏜 경우 점수 계산
        if arrows == n:
            r, a = 0, 0  # r과 a는 각각 라이언과 어피치의 점수
            for i in range(11):
                if ryan[i] > info[i]:  # 라이언이 이긴 경우
                    r += 10 - i
                elif info[i] != 0 and ryan[i] <= info[i]:  # 어피치가 이긴 경우
                    a += 10 - i

            if r > a:  # 라이언이 어피치를 이겼다면
                score_diff = r - a
                if score_diff > max_diff:
                    max_diff = score_diff
                    answer = ryan[:]
                elif score_diff == max_diff:  # 낮은 점수를 더 많이 맞힌 경우를 우선
                    for i in range(10, -1, -1):
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
                        elif ryan[i] < answer[i]:
                            break
            return

        # 각 점수 구간에서 화살을 쏠 수 있는 모든 경우 탐색
        for j in range(idx, 11):
            if ryan[j] <= info[j]:  # 화살 개수가 가능한지 확인
                ryan[j] += 1
                dfs(arrows + 1, j)
                ryan[j] -= 1  # 백트래킹으로 원상복구

    dfs(0, 0)

    # 최대 점수 차이가 0이면 라이언이 이길 수 없는 경우
    return answer if max_diff > 0 else [-1]
