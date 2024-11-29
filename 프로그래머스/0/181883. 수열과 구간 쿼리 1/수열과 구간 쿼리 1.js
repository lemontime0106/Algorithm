function solution(arr, queries) {
    var answer = arr;
    
    for (let query of queries) {
        const [s, e] = query
        
        for (let i=s; i <= e; i++) {
            arr[i]++
        }
    } 
    return answer;
}