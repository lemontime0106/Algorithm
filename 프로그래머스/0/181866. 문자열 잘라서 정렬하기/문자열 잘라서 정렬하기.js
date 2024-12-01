function solution(myString) {
    var answer = myString.split("x").filter(a => a !== "");
    
    return answer.sort((a, b) => (a < b ? -1 : 1));
}