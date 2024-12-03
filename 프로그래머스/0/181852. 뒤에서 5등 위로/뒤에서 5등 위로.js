function solution(num_list) {
    var answer = num_list;
    
    answer.sort((a, b) => a - b);
    
    return answer.slice(5);
}