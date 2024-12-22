function solution(chicken) {
    var answer = 0;
    while (chicken >= 10) {
        let cur = Math.floor(chicken / 10);
        answer += cur
        chicken = chicken % 10 + cur
    }
    return answer;
}