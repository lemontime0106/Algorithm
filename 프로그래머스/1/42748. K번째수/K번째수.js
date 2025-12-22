function solution(array, commands) {
    var answer = [];
    
    for (command of commands) {
        const [i, j, k] = command
        
        const temp = []
        
        for (idx = i-1; idx < j; idx++) {
            temp.push(array[idx])
        }
        
        temp.sort((a, b) => a - b)
        
        answer.push(temp[k-1])
    }
    
    return answer;
}