from collections import deque

N, K = map(int, input().split())
lst = deque(map(int, input().split()))
robot = deque([0] * N)
cnt = 1

while True:
    # 벨트 돌리기
    lst.rotate(1)
    robot.rotate(1)
    robot[N-1] = 0

    # 로봇 움직이기
    for i in range(N-1, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and lst[i+1] > 0:
            robot[i], robot[i+1] = 0, 1
            lst[i+1] -= 1
    robot[N-1] = 0

    # 로봇 올리기
    if robot[0] == 0 and lst[0] > 0:
        robot[0] = 1
        lst[0] -= 1

    # 종료조건 검사
    if lst.count(0) >= K:
        break
    # 아니면 +1
    cnt += 1

# print(lst)
# print(robot)
print(cnt)