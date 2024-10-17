function solution(str1, str2) {
    var answer = [];
    
    const len = str1.length
    
    for (let i=0; i < len; i++) {
        answer.push(str1[i])
        answer.push(str2[i])
    }
    
    return answer.join("");
}