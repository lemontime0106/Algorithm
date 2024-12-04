function solution(arr, k) {
    var answer = [];
    
    for (let i of arr) {
        if (k % 2 === 0) {
            answer.push(i + k)
        } else {
            answer.push(i * k)
        }
    }
    
    return answer;
}