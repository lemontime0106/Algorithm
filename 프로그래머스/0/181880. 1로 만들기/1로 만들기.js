function solution(num_list) {
    var answer = 0;
    
    for (let i of num_list) {
        let temp = i
        
        while (temp !== 1) {
            if (temp % 2 === 0) {
                temp /= 2
                answer++
            } else {
                temp = (temp - 1) / 2
                answer++
            }
        }
    }
    
    return answer;
}