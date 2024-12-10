function solution(hp) {
    var answer = 0;
    
    answer += Math.floor(hp / 5);
    hp -= Math.floor(hp / 5) * 5; 
    
    answer += Math.floor(hp / 3);
    hp -= Math.floor(hp / 3) * 3;
    
    answer += hp; 
    
    return answer;
}