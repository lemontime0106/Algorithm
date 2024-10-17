function solution(l, r) {
    var answer = [];
    
    const isValid = (num) => {
        let numStr = String(num);
        for (let i of numStr) {
            if (i !== "5" && i !== "0") {
                return false;
            }
        }
        return true;
    }
    
    for (let i = l; i <= r; i++) {
        if (isValid(i)) {
            answer.push(i)
        }
    }
    
    return answer.length > 0 ? answer : [-1];
}