function solution(my_string, target) {
    var answer = 0;
    
    if (my_string.includes(target, 0)) {
        answer = 1
    }
    
    return answer;
}