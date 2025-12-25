function solution(s) {
    var answer = 0;
    
    const n = s.length
    
    let temp = ""
    let cnt = 0
    let diff = 0
    
    for (i = 0; i < n; i++) {
        if (temp == "") {
            temp = s[i];
            cnt = 1;
            diff = 0;
        } else {
            if (temp === s[i]) {
                cnt++;
            } else {
                diff++;    
            }
            
            if (cnt == diff) {
                answer++;
                temp = "";
            }   
        }
    }

    if (temp !== "") answer++
    
    return answer;
}