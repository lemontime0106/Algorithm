function solution(quiz) {
    var answer = [];
    
    for (let q of quiz) {
        const formula = q.split(" ")
        const num1 = Number(formula[0])
        const num2 = Number(formula[2])
        const op = formula[1]
        const ans = Number(formula[4])
        
        if (op === "+") {
            if (num1 + num2 === ans) {
                answer.push("O")
            } else {
                answer.push("X")
            }
        } else {
            if (num1 - num2 === ans) {
                answer.push("O")
            } else {
                answer.push("X")
            }
        }
        
    }
    
    return answer;
}