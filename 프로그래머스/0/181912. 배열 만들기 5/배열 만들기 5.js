function solution(intStrs, k, s, l) {
    var answer = [];
    
    for (let i=0; i < intStrs.length; i++) {
        const word = intStrs[i]
        let temp = ""
        for (let j=s; j < s + l; j++) {
            temp += word[j]
        }
        
        if (Number(temp) > k) {
            answer.push(Number(temp))
        }
    }
    
    return answer;
}