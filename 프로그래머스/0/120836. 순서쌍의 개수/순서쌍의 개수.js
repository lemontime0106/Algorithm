function solution(n) {
    var answer = 0;
    
    for (let i = 1; i * i <= n; i++) {
        if (n % i === 0) {
            if (i * i === n) {
                answer += 1;
            } else {
                answer += 2;
            }
        }
    }

    return answer;
}
