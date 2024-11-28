function solution(arr, intervals) {
    var answer = [];
    
    for (let interval of intervals) {
        const [a, b] = interval
        
        for (let i = a; i <= b; i++) {
            answer.push(arr[i])
        }
    }
    
    return answer;
}