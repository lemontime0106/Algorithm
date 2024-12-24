function solution(i, j, k) {
    var answer = 0;
    
    for (let num=i; num <= j; num++) {
        const temp = num
        for (let n of String(temp)) {
            if (n === String(k)) {
                answer++
            }
        }
    }
    
    return answer;
}