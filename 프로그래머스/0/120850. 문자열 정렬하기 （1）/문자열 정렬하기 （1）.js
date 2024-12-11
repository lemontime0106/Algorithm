function solution(my_string) {
    var answer = [];
    
    for (let str of my_string) {
        if (!isNaN(str)) {
            answer.push(parseInt(str));
        }
    }
    
    answer.sort((a, b) => a - b);
    return answer;
}
