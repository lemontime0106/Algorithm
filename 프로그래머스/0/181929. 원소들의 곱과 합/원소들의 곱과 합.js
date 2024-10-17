function solution(num_list) {
    var answer = 0;
    
    let time = 1;
    let pow = 0;
    
    for (let i of num_list) {
        time *= i;
        pow += i;
    }
    
    pow = pow ** 2
    
    if (time > pow) {
        return 0
    } else {
        return 1
    }
    
    return answer;
}