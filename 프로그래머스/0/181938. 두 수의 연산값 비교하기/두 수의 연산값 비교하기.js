function solution(a, b) {
    const first = String(a) + String(b)
    const second = 2 * Number(a) * Number(b)
    
    const answer = Math.max(Number(first), Number(second))
    
    return answer;
}