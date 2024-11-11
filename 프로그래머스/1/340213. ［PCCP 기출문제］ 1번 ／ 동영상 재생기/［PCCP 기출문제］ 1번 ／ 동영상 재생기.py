def solution(video_len, pos, op_start, op_end, commands):
    mm, ss = map(int, pos.split(":"))
    end_mm, end_ss = map(int, video_len.split(":"))
    op_start_mm, op_start_ss = map(int, op_start.split(":"))
    op_end_mm, op_end_ss = map(int, op_end.split(":"))
    
    total_time = end_mm * 60 + end_ss
    pos_time = mm * 60 + ss
    start_time = op_start_mm * 60 + op_start_ss
    end_time = op_end_mm * 60 + op_end_ss
    
    if start_time <= pos_time <= end_time:
        pos_time = end_time
    
    for command in commands:
        if command == "next":
            pos_time += 10
            if pos_time >= total_time:
                pos_time = total_time
        
        else:
            pos_time -= 10
            if pos_time < 0:
                pos_time = 0
        
        if start_time <= pos_time <= end_time:
            pos_time = end_time
        
    answer = [str(pos_time // 60).zfill(2), str(pos_time % 60).zfill(2)]
    
    answer_time = ":".join(answer)
    
    return answer_time