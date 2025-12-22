function solution(numbers) {
    var answer = '';
    
    numbers.sort((a, b) => {
        const ab = "" + a + b
        const ba = "" + b + a
        
        if (ab > ba) {
            return -1
        } else if (ab < ba) {
            return 1
        } else {
            return 0
        }
    })
    
    for (number of numbers) {
        answer += number
    }
    
    if (numbers[0] === 0) {
        return "0"
    }
    
    return answer;
}