function solution(emergency) {
    var answer = new Array(emergency.length).fill(0);

    let sorted = [...emergency].sort((a, b) => b - a);
    
    for (let i = 0; i < emergency.length; i++) {
        answer[emergency.indexOf(sorted[i])] = i + 1;
    }

    return answer;
}