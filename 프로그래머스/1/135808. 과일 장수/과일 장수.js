function solution(k, m, score) {
    var answer = 0;
    
    score = score.sort((a, b) => b-a)
    
    let cnt = 0
    
    for (let i=0; i < score.length; i++) {
        cnt++
        
        if (cnt == m) {
            answer += score[i] * m
            cnt = 0
        }
    }
    
    return answer;
}