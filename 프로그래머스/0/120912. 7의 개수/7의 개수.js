function solution(array) {
    var answer = 0;
    
    for (let num of array) {
        for (let i of String(num)) {
            if (i === "7") {
                answer += 1
            }
        }
    }
    
    return answer;
}