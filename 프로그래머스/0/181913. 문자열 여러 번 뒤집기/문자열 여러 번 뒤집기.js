function solution(my_string, queries) {
    var answer = my_string;
    
    for (let query of queries) {
        const [a,b] = query
        
        let head = ""
        let tail = ""
        let temp = ""
        
        for (let i = 0; i < a; i++) {
            head += answer[i]
        }
        
        for (let i = b + 1; i < answer.length; i++) {
            tail += answer[i]
        }
        
        for (let i = b; i >= a; i--) {
            temp += answer[i]
        }
        
        answer = head + temp + tail
    }
    
    return answer;
}