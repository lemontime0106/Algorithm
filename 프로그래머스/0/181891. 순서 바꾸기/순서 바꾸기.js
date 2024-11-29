function solution(num_list, n) {
    var answer = [];
    
    let new_list = []
    
    for (let i = 0; i < 2; i++) {
        for (let j of num_list) {
            new_list.push(j)
        }
    }
    
    for (let i=n; i < n+num_list.length; i++) {
        answer.push(new_list[i])
    }
    
    return answer;
}