function isYellow(time, green, yellow, red) {
    const cycle = green + yellow + red
    const pos = (time - 1) % cycle
    
    return green <= pos && pos < green + yellow
}

function solution(signals) {
    var answer = 0;
    
    const temp = []
    
    for (const signal of signals) {
        let sum = 0
        
        for (const v of signal) {
            sum += v
        }
        
        temp.push(sum)
    }
    
    let maxNum = 1
    for (const i of temp) {
        maxNum *= i
    }
    
    for (let i = 1; i < maxNum; i++) {
        let flag = true
        
        for (const [g, y, r] of signals) {
            if (!isYellow(i, g, y, r)) {
                flag = false
                break
            }
        }
        
        if (flag) {
            return i;
        }
    }
    
    return -1;
}