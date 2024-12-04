function solution(n) {
    var answer = [];
    
    for (let i = 0; i < n; i++) {
        let array = new Array(n).fill(0)
        array[i] = 1
        answer.push(array)
    }
    
    return answer;
}