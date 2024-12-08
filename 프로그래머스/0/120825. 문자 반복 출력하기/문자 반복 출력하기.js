function solution(my_string, n) {
    var answer = '';
    
    for (let str of my_string) {
        for (let i=0; i < n; i++) {
            answer += str
        }
    }
    
    return answer;
}