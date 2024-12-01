function solution(binomial) {
    const number = binomial.split(" ")
    
    const [a, op, b] = [...number]
    
    if (op === "+") {
        return Number(a) + Number(b)
    } else if (op === "-") {
        return Number(a) - Number(b)
    } else if (op === "*") {
        return Number(a) * Number(b)
    }
}