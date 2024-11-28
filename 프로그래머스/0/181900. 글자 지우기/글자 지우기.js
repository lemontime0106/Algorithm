function solution(my_string, indices) {
    var answer = my_string.split("");
    
    for (let i of indices) {
        answer[i] = "";
    }
    
    return answer.join("");
}