from collections import deque

# 초기 상태를 입력받음
MAP = [list(map(int, input().split())) for _ in range(3)]

# 목표 상태 정의
goal = '123456780'

# 초기 상태를 문자열로 변환
start = ''.join(str(MAP[i][j]) for i in range(3) for j in range(3))

# 이동 방향 정의 (상, 하, 좌, 우)
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 빈 칸(0)의 위치 찾기
zero_pos = start.index('0')

# BFS를 위한 큐 초기화
q = deque([(start, zero_pos, 0)])

# 방문한 상태를 추적하기 위한 집합
visited = set()
visited.add(start)

while q:
    current_state, zero_pos, cnt = q.popleft()
    
    # 현재 상태가 목표 상태인지 확인
    if current_state == goal:
        print(cnt)
        break
    
    # 빈 칸의 좌표 계산
    x, y = divmod(zero_pos, 3)
    
    # 네 방향으로 이동 시도
    for d in direct:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < 3 and 0 <= ny < 3:
            # 새로운 빈 칸의 위치
            new_zero_pos = nx * 3 + ny
            # 새로운 상태 만들기
            new_state = list(current_state)
            new_state[zero_pos], new_state[new_zero_pos] = new_state[new_zero_pos], new_state[zero_pos]
            new_state = ''.join(new_state)
            
            # 새로운 상태가 방문한 적 없는 상태라면 큐에 추가
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, new_zero_pos, cnt + 1))
else:
    # 목표 상태에 도달할 수 없는 경우
    print(-1)
