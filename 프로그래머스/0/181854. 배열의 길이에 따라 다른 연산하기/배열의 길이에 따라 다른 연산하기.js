function solution(arr, n) {
    var answer = arr;
    
    if (answer.length % 2 === 0) {
        for (let i in answer) {
            if (i % 2 === 1) {
                answer[i] += n
            }
        }
    } else {
        for (let i in answer) {
            if (i % 2 === 0) {
                answer[i] += n
            }
        }
    }
    
    return answer;
}