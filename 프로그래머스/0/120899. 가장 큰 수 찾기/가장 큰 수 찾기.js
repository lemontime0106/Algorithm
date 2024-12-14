function solution(array) {
    var answer = [0, 0];
    
    for (let i in array) {
        if (array[i] > answer[0]) {
            answer[0] = array[i]
            answer[1] = parseInt(i)
        }
    }
    
    return answer;
}