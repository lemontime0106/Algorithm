function solution(arr, k) {
    var answer = [];
    
    for (let i of arr) {
        if (!answer.includes(i)) {
            answer.push(i)
        }
        
        if (answer.length === k) {
            break
        }
    }
    
    while (answer.length !== k) {
        answer.push(-1)
    }
    
    return answer;
}