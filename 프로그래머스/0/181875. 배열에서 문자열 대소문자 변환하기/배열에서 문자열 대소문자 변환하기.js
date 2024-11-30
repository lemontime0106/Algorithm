function solution(strArr) {
    var answer = [...strArr];
    
    for (let i in answer) {
        if (i % 2 === 1) {
            answer[i] = answer[i].toUpperCase();
        } else {
            answer[i] =answer[i].toLowerCase();
        }
    }
    
    return answer;
}