function solution(n, control) {
    var answer = n;
    
    for (let i of control) {
        if (i === "w") {
            answer += 1
        } else if (i === "s") {
            answer -= 1
        } else if (i === "d") {
            answer += 10
        } else if (i === "a") {
            answer -= 10
        }
    }
    
    return answer;
}