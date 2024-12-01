function solution(myString, pat) {
    var answer = 0;
    
    let reverse = ""
    
    for (let str of myString) {
        if (str === "A") {
            reverse += "B"
        } else {
            reverse += "A"
        }
    }
    
    if (reverse.includes(pat)) {
        return 1
    } else {
        return 0
    }
    
    return answer;
}