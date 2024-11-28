function solution(arr, idx) {
    var answer = [];
    
    for (let i = idx; i < arr.length; i++) {
        if (arr[i] === 1) {
            answer.push(i);
        }
    }
    
    if (answer.length === 0) {
        return -1;
    }
    
    return Math.min(...answer);
}