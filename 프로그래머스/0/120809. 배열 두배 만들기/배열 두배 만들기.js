function solution(numbers) {
    var answer = numbers;
    
    for (let i in answer) {
        answer[i] *= 2
    }
    
    return answer;
}