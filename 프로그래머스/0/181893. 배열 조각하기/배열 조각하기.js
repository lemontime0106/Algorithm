function solution(arr, query) {
    var answer = arr;
    
    for (let i in query) {
        if (i % 2 === 0) {
            answer = answer.slice(0, query[i]+1)
        } else {
            answer = answer.slice(query[i])
        }
    }
    
    return answer;
}