function solution(num_list) {
    var answer = [];
    
    const sort_list = num_list.sort((a, b) => a - b)
    
    for (let i = 0; i < 5; i++) {
        answer.push(sort_list[i])
    }
    
    return answer;
}