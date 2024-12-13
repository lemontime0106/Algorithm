function solution(my_string) {
    var answer = '';
    
    for (let s of my_string) {
        if (!answer.includes(s)) {
            answer += s
        }
    }
    
    return answer;
}