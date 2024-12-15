function solution(n) {
    var answer = 2;
    
    for (let i = 0; i <= 1000; i++) {
        if (i ** 2 === n) {
            answer = 1
            break
        }
    }
    
    return answer;
}