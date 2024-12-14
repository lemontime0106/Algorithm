function solution(my_string) {    
    const expression = my_string.split(" ")
    var answer = Number(expression[0]);
    let op = ""
    
    for (let i=1; i < expression.length; i++) {
        if (expression[i] === "+") {
            op = "+"
        } else if (expression[i] === "-") {
            op = "-"
        } else {
            if (op === "+") {
                answer += Number(expression[i])
            } else {
                answer -= Number(expression[i])
            }
        }
    }
    
    
    
    return answer;
}