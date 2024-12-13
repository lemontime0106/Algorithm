function solution(order) {
    var answer = 0;
    
    const number = String(order)
    
    for (let i of number) {
        if (i === "3" || i === "6" || i === "9") {
            answer++
        }
    }
    
    return answer;
}