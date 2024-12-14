function solution(s) {
    var answer = [];
    
    let dict = {}
    
    for (let i of s) {
        if (dict[i] === undefined) {
            dict[i] = 1
        } else {
            dict[i]++
        }
    }
    
    for (let key in dict) {
        if (dict[key] === 1) {
            answer.push(key)
        }
    }
    
    answer.sort()
    
    return answer.join("");
}