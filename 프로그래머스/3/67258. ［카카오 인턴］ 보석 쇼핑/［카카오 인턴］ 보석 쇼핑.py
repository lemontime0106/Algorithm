def solution(gems):
    gem_types = len(set(gems))  # 보석 종류의 수
    gem_count = {}
    start, end = 0, 0
    answer = [0, len(gems) - 1]
    
    while end < len(gems):
        # 현재 end가 가리키는 보석을 gem_count에 추가
        if gems[end] in gem_count:
            gem_count[gems[end]] += 1
        else:
            gem_count[gems[end]] = 1
        
        # 모든 종류의 보석을 포함하고 있는지 확인
        while len(gem_count) == gem_types:
            # 현재 구간이 더 짧다면 갱신
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
            
            # 구간을 줄이기 위해 start 포인터 이동
            if gem_count[gems[start]] == 1:
                del gem_count[gems[start]]
            else:
                gem_count[gems[start]] -= 1
            start += 1
        
        # end 포인터를 이동시켜 다음 보석을 포함
        end += 1
    
    return [answer[0] + 1, answer[1] + 1]
