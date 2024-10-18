function solution(s) {
    var answer = true;

    let stack = [];
    
    for (let i of s) {
        if (i === "(") {
            stack.push(i);
        } else if (i === ")") {
            if (stack.length === 0 || stack[stack.length - 1] !== "(") {
                return false;
            }
            stack.pop();
        }
    }
    
    if (stack.length !== 0) {
        answer = false;
    }
    
    return answer;
}