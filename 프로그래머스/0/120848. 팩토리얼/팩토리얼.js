function solution(n) {
    var answer = 0;
    
    for (let i = 1; i <= 10; i++) {
        let temp = 1
        
        for (let j=1; j <= i; j++) {
            temp *= j
        }
        
        if (temp <= n) {
            answer = i
        }
    }
    
    return answer;
}