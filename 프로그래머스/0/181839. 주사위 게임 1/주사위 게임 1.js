function solution(a, b) {
    var answer = 0;
    
    if (a % 2 == 0 && b % 2 == 0) {
        return Math.abs(a - b)
    } else if (a % 2 == 1 && b % 2 == 1) {
        return Math.pow(a, 2) + Math.pow(b, 2)
    } else {
        return 2 * (a + b)
    }
    
    return answer;
}