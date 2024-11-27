function solution(arr, queries) {
    var answer = arr;
    
    for (let query of queries) {
        const [s, e, k] = query
        
        for (let i = s; i < e+1; i++) {
            if (i % k === 0) {
                answer[i]++
            }
        }
    }
    
    return answer;
}