function solution(n) {
    var answer = [];
    
    for (let i = 2; i <= Math.sqrt(n); i++) {
        while (n % i === 0) { 
            if (!answer.includes(i)) {
                answer.push(i);
            }
            n = n / i;
        }
    }

    if (n > 1) {
        answer.push(n);
    }
    
    return answer.sort((a, b) => a - b);
}
