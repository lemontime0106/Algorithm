function solution(babbling) {
    var answer = 0;
    
    const possible = ["aya", "ye", "woo", "ma"];
    
    for (let b of babbling) {
        let temp = b;
        
        for (let p of possible) {
            if (temp.includes(p + p)) {
                break;
            }
            temp = temp.split(p).join(" ");
        }
        
        if (temp.trim() === "") {
            answer++;
        }
    }
    
    return answer;
}
