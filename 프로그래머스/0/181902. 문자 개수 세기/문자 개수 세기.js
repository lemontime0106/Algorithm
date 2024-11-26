function solution(my_string) {
    var answer = Array(52).fill(0);
    
    for (let i=0; i < my_string.length; i++) {
        let alpha = my_string.charCodeAt(i);
        if (alpha <= 90) {
            answer[alpha-65]++
        } else {
            answer[alpha-71]++
        }
    }
    
    return answer;
}