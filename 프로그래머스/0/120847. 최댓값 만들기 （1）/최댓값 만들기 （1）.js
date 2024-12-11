function solution(numbers) {    
    numbers.sort((a, b) => a - b);
    
    const a = numbers.pop()
    const b = numbers.pop()
    
    return a * b;
}