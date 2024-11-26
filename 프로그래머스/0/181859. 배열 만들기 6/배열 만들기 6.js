function solution(arr) {
    var stk = [];
    let i = 0;
    
    while (i < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[i])
            i++
        } else {
            let N = stk.length;
            if (stk[N-1] === arr[i]) {
                stk.pop()
                i++
            } else {
                stk.push(arr[i])
                i++
            }
        }
    }
    
    if (stk.length === 0) {
        stk = [-1]
    }
    
    return stk;
}