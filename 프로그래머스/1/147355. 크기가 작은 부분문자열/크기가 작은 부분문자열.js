function solution(t, p) {
    var answer = 0;
    
    const lenT = t.length
    const lenP = p.length
    
    for (let i=0; i < (lenT - lenP + 1); i++) {
        let temp = ""
        
        for (let j=0; j < lenP; j++ ) {
            temp += t[i+j]
        }
        
        if (Number(temp) <= Number(p) ) {
            answer++
        }
    }
    
    return answer;
}