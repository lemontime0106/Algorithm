function solution(rny_string) {
    var answer = '';
    
    for (let str of rny_string) {
        if (str === "m") {
            answer += "rn"
        } else {
            answer += str
        }
    }
    
    return answer;
}