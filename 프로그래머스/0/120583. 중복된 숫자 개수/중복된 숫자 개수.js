function solution(array, n) {
    var answer = 0;
    
    for (let i of array) {
        if (i === n) {
            answer += 1
        }
    }
    
    return answer;
}