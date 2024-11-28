function solution(arr) {
    var answer = [];
    
    let temp = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 2) {
            temp.push(i)
        }
    }
    
    let min = Math.min(...temp)
    let max = Math.max(...temp)
    
    for (let i = min; i <= max; i++) {
        answer.push(arr[i])
    }
    
    if (answer.length === 0) {
        return [-1]
    }
    
    return answer;
}