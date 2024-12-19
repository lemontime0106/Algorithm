function solution(a, b) {
    function gcd(x, y) {
        while (y !== 0) {
            let temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }

    const gcdValue = gcd(a, b);
    let denominator = b / gcdValue;

    while (denominator % 2 === 0) denominator /= 2;
    while (denominator % 5 === 0) denominator /= 5;

    return denominator === 1 ? 1 : 2;
}
