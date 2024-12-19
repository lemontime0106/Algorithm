function solution(n) {
    let answer = 0; 
    for (let i = 1; answer < n; i++) {
        if (String(i).includes("3") || i % 3 === 0) {
            continue;
        }
        answer++;
        if (answer === n) {
            return i;
        }
    }
}
