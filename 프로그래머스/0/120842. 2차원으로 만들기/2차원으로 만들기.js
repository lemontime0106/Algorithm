function solution(num_list, n) {
    var answer = [];
    
    const N  = parseInt(num_list.length / n)
    
    for (let i = 0; i < N; i++) {
        let temp = []
        for (let j=0; j < n; j++) {
            temp.push(num_list[n*i + j])
        }
        answer.push(temp)
    }
    
    return answer;
}