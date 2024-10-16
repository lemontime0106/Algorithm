function solution(a, b, c, d) {
    let answer = 0;
    
    dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    let lst = [a, b, c, d]
    
    for(const i of lst) {
        dict[i] += 1
    }
    
    let freq = Object.values(dict).filter(x => x > 0);
    let keys = Object.keys(dict).map(Number).filter(x => dict[x] > 0);
    
    if (freq.length === 1) {
        answer = 1111 * keys[0]
    } else if (freq.length === 2) {
        if (freq.includes(3)) {
            let p = keys.find(k => dict[k] === 3);
            let q = keys.find(k => dict[k] === 1);
            answer = Math.pow((10 * p + q), 2);
        } else {
            let p = keys[0];
            let q = keys[1];
            answer = (p + q) * Math.abs(p - q);
        }
    } else if (freq.length === 3) {
        let p = keys.find(k => dict[k] === 2);
        let q = keys.find(k => dict[k] === 1);
        let r = keys.find(k => dict[k] === 1 && k !== q);
        answer = q * r
    } else {
        answer = Math.min(a, b, c, d)
    }
    
    return answer;
}