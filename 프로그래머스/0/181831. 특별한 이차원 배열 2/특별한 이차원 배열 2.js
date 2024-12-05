function solution(arr) {
    var answer = 0;
    const N = arr.length
    let flag = true
    for (let i=0; i < N; i++) {
        for (let j=0; j<N; j++) {
            if (arr[i][j] !== arr[j][i]) {
                flag = false
            }
            
            if (!flag) {
                break
            }
        }
        if (!flag) {
            break
        }
    }
    
    return flag ? 1 : 0;
}