function solution(array, n) {
    let answer = 0;
    let temp = Infinity;

    for (let a of array) {
        const abs = Math.abs(a - n);
        if (abs < temp || (abs === temp && a < answer)) {
            temp = abs;
            answer = a;
        }
    }

    return answer;
}
