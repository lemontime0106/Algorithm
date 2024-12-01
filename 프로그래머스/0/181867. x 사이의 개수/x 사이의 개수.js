function solution(myString) {
    var answer = [];
        
    const temp = myString.split("x")
    
    for (let t of temp) {
        answer.push(t.length)    
    }
    
    return answer;
}