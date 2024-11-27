function solution(x1, x2, x3, x4) {
    var answer = true;
    
    let case1 = (x1 || x2)
    let case2 = (x3 || x4)
    
    answer = (case1 && case2)
    
    return answer;
}