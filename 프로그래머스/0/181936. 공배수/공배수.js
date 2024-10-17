function solution(number, n, m) {
    let answer = 0
    
    const remain1 = number % n
    const remain2 = number % m
    
    if (remain1 === 0 && remain2 === 0) {
        answer = 1
    }
    
    return answer;
}