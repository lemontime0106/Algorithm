def solution(brown, yellow):
    total = brown + yellow
    
    # total의 약수를 구해서 가능한 가로, 세로를 확인
    for height in range(3, int(total**0.5) + 1):
        if total % height == 0:
            width = total // height
            # 갈색 타일과 노란색 타일의 조건을 만족하는지 확인
            if (width - 2) * (height - 2) == yellow:
                return [width, height]