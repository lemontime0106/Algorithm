function solution(numbers, n) {
    var answer = 0;
    
    for (let i of numbers) {
        answer += i;
        if (answer > n) {
            break
        }; 
    }
    
    return answer;
}