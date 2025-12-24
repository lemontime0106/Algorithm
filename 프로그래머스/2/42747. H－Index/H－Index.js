function solution(citations) {
    let answer = 0;
    
    const temp = citations.sort((a, b) => b - a)
    
    const n = citations.length
    
    for (i=0; i < n; i++) {
        if (temp[i] >= i+1) {
            answer = i+1
        } else {
            break
        }
    }
    
    return answer;
}