function solution(rsp) {
    var answer = '';
    
    const list = rsp.split("")
    
    for (let i of list) {
        if (i === "2") {
            answer += "0"
        } else if (i === "5") {
            answer += "2"
        } else if (i === "0") {
            answer += "5"
        }
    }
    
    return answer;
}