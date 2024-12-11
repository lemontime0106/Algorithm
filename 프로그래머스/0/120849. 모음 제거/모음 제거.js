function solution(my_string) {
    var answer = '';
    const temp = ["a", "e", "i", "o", "u"]
    
    for (let str of my_string) {
        if (!temp.includes(str)) {
            answer += str
        }
    }
    
    return answer;
}