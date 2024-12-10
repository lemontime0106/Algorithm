function solution(numbers, k) {
    let answer = 0; 
    for (let i = 1; i < k; i++) { 
        answer = (answer + 2) % numbers.length;
    }
    return numbers[answer]; 
}
