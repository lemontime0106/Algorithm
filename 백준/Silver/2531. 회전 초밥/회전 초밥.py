N, d, k, c = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

# 슬라이딩 윈도우를 위한 초기 설정
window = [0] * (d + 1)  # 각 초밥의 종류가 현재 윈도우에 몇 개 있는지 저장하는 배열
current_count = 0

# 처음 k개의 초밥을 윈도우에 추가
for i in range(k):
    if window[lst[i]] == 0:
        current_count += 1
    window[lst[i]] += 1

# 쿠폰으로 먹는 초밥이 현재 윈도우에 포함되지 않았다면, 포함시키기
answer = current_count
if window[c] == 0:
    answer += 1

# 슬라이딩 윈도우 시작
for i in range(1, N):
    # 윈도우의 오른쪽에 새로 들어오는 초밥 추가
    new_sushi = lst[(i + k - 1) % N]
    if window[new_sushi] == 0:
        current_count += 1
    window[new_sushi] += 1

    # 윈도우의 왼쪽에서 빠져나가는 초밥 제거
    old_sushi = lst[i - 1]
    window[old_sushi] -= 1
    if window[old_sushi] == 0:
        current_count -= 1

    # 쿠폰으로 먹는 초밥 포함 여부 확인 후 최대값 갱신
    if window[c] == 0:
        answer = max(answer, current_count + 1)
    else:
        answer = max(answer, current_count)

print(answer)
