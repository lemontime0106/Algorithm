function solution(num, n) {
    const value = num % n
    
    let answer = 1
    
    if (value) {
        answer = 0
    }
    
    return answer;
}