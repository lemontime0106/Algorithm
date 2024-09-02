def solution(genres, plays):
    answer = []
    
    pl = {}
    
    for i in range(len(genres)):
        if genres[i] not in pl:
            pl[genres[i]] = [(i, plays[i])]
        else:
            pl[genres[i]].append((i, plays[i]))
            
    play_cnt = {}
    for genre, songs in pl.items():
        total_cnt = 0
        for song in songs:
            total_cnt += song[1]
        play_cnt[genre] = total_cnt
        
    sorted_genres = sorted(play_cnt.keys(), key=lambda x: play_cnt[x], reverse=True)
    
    for genre in sorted_genres:
        sorted_songs = sorted(pl[genre], key=lambda x: (-x[1], x[0]))
        
        cnt = 0
        for i in sorted_songs:
            if cnt < 2:
                answer.append(i[0])
                cnt += 1
            else:
                break
    return answer