function solution(numLog) {
    var answer = '';
    let temp = numLog[0];
    
    for (let i = 1; i < numLog.length; i++) { 
        const cal = numLog[i] - temp;
        
        if (cal === 1) {
            answer += "w";
        } else if (cal === -1) {
            answer += "s";
        } else if (cal === 10) {
            answer += "d"; 
        } else if (cal === -10) {
            answer += "a"; 
        }
        
        temp = numLog[i];
    }
    
    return answer;
}