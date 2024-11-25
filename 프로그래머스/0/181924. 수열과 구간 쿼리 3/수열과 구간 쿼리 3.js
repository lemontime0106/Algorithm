function solution(arr, queries) {
    var answer = arr;
    
    for (let query of queries) {
        const a = query[0]
        const b = query[1]
        
        let temp = 0
        temp = answer[a]
        answer[a] = answer[b]
        answer[b] = temp
        
    }
    
    return answer;
}