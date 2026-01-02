function solution(s, skip, index) {
    var answer = '';
    
    let alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for (sk of skip) {
        alpha = alpha.replace(sk, "")
    }
    
    const n = alpha.length
    
    for (i of s) {
        answer = answer + alpha[(alpha.indexOf(i) + index) % n]
    }
    
    
    return answer;
}