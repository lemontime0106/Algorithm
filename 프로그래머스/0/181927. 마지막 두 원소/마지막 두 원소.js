function solution(num_list) {
    var answer = num_list;
    const count = num_list.length
    const a = num_list[count - 1]
    const b = num_list[count - 2]
    if (a > b) {
        answer.push(a - b)
    } else {
        answer.push(a * 2)
    }
    
    return answer;
}