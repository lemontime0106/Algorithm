function solution(num_list) {
    var answer = 0;
    
    let odd = 0;
    let even = 0;
    
    for (let i in num_list) {
        if (i % 2 === 0) {
            even += num_list[i]
        } else {
            odd += num_list[i]
        }
    }
    
    answer = Math.max(odd, even)
    
    return answer;
}