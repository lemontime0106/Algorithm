function solution(balls, share) {
    var answer = 0;
    
    let top = 1
    let bottom = 1
    
    for (let i = balls; i > balls - share; i--) {
        top *= i
    }
    
    for (let i = share; i > 0; i--) {
        bottom *= i
    }
    
    answer = Math.floor(top / bottom)
    
    return answer;
}