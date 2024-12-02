function solution(strArr) {
    var answer = 0;
    let len = 0;
    
    for (let str of strArr) {
        if (len < str.length) {
            len = str.length
        }
    }
    
    for (let i = 1; i <= len; i++) {
        let temp = 0
        for (let str of strArr) {
            if (str.length === i) {
                temp++
            }
        }
        if (temp > answer) {
            answer = temp
        }
    }
    
    return answer;
}