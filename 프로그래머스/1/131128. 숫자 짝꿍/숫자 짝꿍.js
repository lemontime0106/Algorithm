function solution(X, Y) {
    var answer = '';
    
    const temp = []
    const yCount = Array(10).fill(0)
    
    for (const y of Y) {
        yCount[y]++
    }
    
    for (const i of X) {
        if (yCount[i] > 0) {
            temp.push(i)
            yCount[i]--
        }
    }
    
    if (temp.length === 0) {
        return "-1"
    } else if (temp.length === 1) {
        return temp[0]
    }
    
    temp.sort((a, b) => b - a)
    
    if (temp[0] === "0") {
        return "0"
    }
    
    answer = temp.join("")
    return answer
}
