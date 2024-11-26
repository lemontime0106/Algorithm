function solution(arr) {
    var stk = [];
    var i = 0;

    while (i < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[i]);
            i++;
        } else {
            let N = stk.length;
            if (stk[N - 1] < arr[i]) {
                stk.push(arr[i]);
                i++;
            } else {
                stk.pop();
            }
        }
    }

    return stk; // 최종 결과 반환
}
