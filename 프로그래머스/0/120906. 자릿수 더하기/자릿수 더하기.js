function solution(n) {
    var answer = 0;
    const nStr = String(n)
    
    for (let num of nStr) {
        answer += Number(num)
    }
    
    return answer;
}