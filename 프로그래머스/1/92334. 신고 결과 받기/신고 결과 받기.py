def solution(id_list, report, k):
    # 중복 신고 제거
    report = set(report)
    
    # id_list의 각 아이디에 대한 인덱스를 저장하는 사전
    index_dict = {id: idx for idx, id in enumerate(id_list)}
    
    report_count = [0] * len(id_list)  # 각 사용자별 신고 받은 횟수
    reported_by = [[] for _ in range(len(id_list))]  # 누가 누구를 신고했는지 저장
    
    for rep in report:
        reporter, reportee = rep.split()
        if reportee not in reported_by[index_dict[reporter]]:
            reported_by[index_dict[reporter]].append(reportee)
            report_count[index_dict[reportee]] += 1
            
    # k번 이상 신고된 사용자 확인
    bad_users = {id_list[idx] for idx, count in enumerate(report_count) if count >= k}
    
    # 결과 계산
    answer = [0] * len(id_list)
    for idx, reports in enumerate(reported_by):
        answer[idx] = sum(1 for reportee in reports if reportee in bad_users)
        
    return answer