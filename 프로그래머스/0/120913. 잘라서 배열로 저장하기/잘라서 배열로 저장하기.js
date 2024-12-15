function solution(my_str, n) {
    var answer = [];
    
    let temp = ""
    
    for (let i of my_str) {
        temp += i
        
        if (temp.length === n) {
            answer.push(temp)
            temp = ""
        }
    }
    
    if (temp !== "") {
        answer.push(temp)        
    }
    
    return answer;
}