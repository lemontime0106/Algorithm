function solution(arr) {
    var answer = [];
    
    for (let i in arr) {
        if (arr[i] % 2 === 0 && arr[i] >= 50) {
            answer.push(arr[i] / 2)
        } else if (arr[i] % 2 === 1 && arr[i] < 50) {
            answer.push(arr[i] * 2)
        } else {
            answer.push(arr[i])
        }
    }
    
    return answer;
}