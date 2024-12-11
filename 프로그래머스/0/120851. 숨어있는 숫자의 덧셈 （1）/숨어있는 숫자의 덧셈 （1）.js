function solution(my_string) {
    var answer = 0;
    
    for (let str of my_string) {
        if (!isNaN(str)) {
            answer += parseInt(str)
        }
    }
    
    return answer;
}