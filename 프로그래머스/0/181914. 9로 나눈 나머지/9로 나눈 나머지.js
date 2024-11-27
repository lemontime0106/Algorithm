function solution(number) {
    var answer = 0;
    
    let temp = 0
    
    for (let i=0; i < number.length; i++) {
        temp += Number(number[i])
    }
    
    answer = temp % 9
    
    return answer;
}