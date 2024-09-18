# 입력 처리
N = int(input())  # 용액의 수
lst = list(map(int, input().split()))  # 용액 리스트
lst.sort()  # 정렬된 상태에서 투 포인터 사용

# 초기값 설정
closest_sum = float("inf")
result = []

# 첫 번째 용액을 고정하고 나머지 두 용액을 투 포인터로 찾기
for i in range(N - 2):
    left = i + 1  # 두 번째 용액을 가리키는 포인터
    right = N - 1  # 세 번째 용액을 가리키는 포인터

    while left < right:
        current_sum = lst[i] + lst[left] + lst[right]

        # 현재 세 용액의 합이 0에 더 가까운지 확인
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = [lst[i], lst[left], lst[right]]

        # 합이 음수면 더 큰 값을 만들어야 하므로 left를 이동
        if current_sum < 0:
            left += 1
        # 합이 양수면 더 작은 값을 만들어야 하므로 right를 이동
        else:
            right -= 1

# 결과 출력 (오름차순 정렬)
print(*sorted(result))