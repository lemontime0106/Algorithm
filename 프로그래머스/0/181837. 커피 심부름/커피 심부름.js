function solution(order) {
    var answer = 0;
    
    for (let coffee of order) {
        if (coffee.includes("americano") || coffee.includes("anything")) {
            answer += 4500
        } else if (coffee.includes("cafelatte")) {
            answer += 5000
        }
    }
    
    return answer;
}