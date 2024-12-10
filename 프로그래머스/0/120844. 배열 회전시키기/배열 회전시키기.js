function solution(numbers, direction) {
    var answer = [...numbers];

    if (direction === "left") {
        answer.push(answer.shift())
    } else {
        const last = answer.pop();
        answer = [last, ...answer];
    }
    
    return answer;
}
