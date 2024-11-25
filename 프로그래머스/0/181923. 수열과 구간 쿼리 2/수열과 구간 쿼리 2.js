function solution(arr, queries) {
    var answer = [];
    
    for (let query of queries) {
        const s = query[0]
        const e = query[1]
        const k = query[2]
        
        let temp = 1000001
        
        for (let i = s; i < e+1; i++) {
            if (arr[i] > k && temp > arr[i]) {
                temp = arr[i]
            }
        }
        
        if (temp != 1000001) {
            answer.push(temp)
        } else {
            answer.push(-1)
        }
        
    }
    
    return answer;
}