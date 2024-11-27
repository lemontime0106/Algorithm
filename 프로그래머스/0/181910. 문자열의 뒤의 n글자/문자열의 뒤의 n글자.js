function solution(my_string, n) {
    var answer = '';
    
    const N = my_string.length
    
    for (let i = N-n; i < N; i++) {
        answer += my_string[i]
    }
    
    return answer;
}