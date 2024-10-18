function solution(diffs, times, limit) {
    let left = 1
    let right = 100000
    let mid = undefined
    let answer = right
    
    while (left <= right) {
        mid = Math.floor((left + right) / 2)
        let time = 0, flag = false
        for (let i = 0; i<diffs.length; ++i) {
            if (mid - diffs[i] < 0) {
                time = time + (diffs[i]-mid) * (times[i] + times[i-1]) + times[i]
            } else {
                time += times[i]
            }
            
            if (limit < time) {
                flag = true
                break
            }
        }
        
        if (flag) {
            left = mid + 1
        } else {
            answer = mid
            right = mid - 1
        }
    } 
        
    return answer;
}