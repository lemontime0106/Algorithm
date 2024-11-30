function solution(my_string, alp) {
    var answer = '';
    
    for (let i in my_string) {
        if (my_string[i] === alp) {
            answer += alp.toUpperCase()
        } else {
            answer += my_string[i]
        }
    }
    
    return answer;
}