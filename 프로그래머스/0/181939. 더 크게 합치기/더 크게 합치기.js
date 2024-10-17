function solution(a, b) {
    const first = String(a) + String(b)
    const second = String(b) + String(a)
    
    const answer = Math.max(Number(first), Number(second))
    
    return answer;
}