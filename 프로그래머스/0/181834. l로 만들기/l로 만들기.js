function solution(myString) {
    var answer = '';
    const code = "l".charCodeAt()
    
    for (let str of myString) {
        if (str.charCodeAt() > code) {
            answer += str
        } else {
            answer += "l"
        }
    }
        
    return answer;
}