function solution(num_list) {
    var answer = 0;
    let odd = ""
    let even = ""
    
    for (i of num_list) {
        if (i % 2 == 0) {
            even += i
        } else {
            odd += i
        }
    }
    
    answer = Number(odd) + Number(even)
    
    return answer;
}