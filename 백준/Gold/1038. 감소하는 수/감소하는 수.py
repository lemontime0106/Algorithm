from itertools import combinations

N = int(input())

# 모든 감소하는 수를 저장할 리스트
decreasing_numbers = []

# 1자리부터 10자리까지의 감소하는 수를 생성
for length in range(1, 11):
    # 0부터 9까지의 숫자 중 length개를 선택하여 조합 생성
    for comb in combinations(range(10), length):
        # 내림차순으로 정렬하여 감소하는 수를 만듦
        num_str = ''.join(map(str, sorted(comb, reverse=True)))
        decreasing_numbers.append(int(num_str))

# 감소하는 수들을 오름차순으로 정렬
decreasing_numbers.sort()

# N번째 감소하는 수를 찾기
if N >= len(decreasing_numbers):
    print(-1)  # N번째 감소하는 수가 없으면 -1 출력
else:
    print(decreasing_numbers[N])
