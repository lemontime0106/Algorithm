function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}

function solution(numer1, denom1, numer2, denom2) {
    var answer = [];

    let numer = numer1 * denom2 + numer2 * denom1;
    let denom = denom1 * denom2;
    
    const G = gcd(numer, denom);
    
    answer = [numer / G, denom / G];
    
    return answer;
}
