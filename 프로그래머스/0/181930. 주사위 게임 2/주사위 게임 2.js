function solution(a, b, c) {
    var answer = 0;
    dict = {}
    
    dict[a] = (dict[a] || 0) + 1
    dict[b] = (dict[b] || 0) + 1
    dict[c] = (dict[c] || 0) + 1
    
    var freq = Object.keys(dict).length;
    var keys = Object.keys(dict);
    
    if (freq === 1) {
        const p = Number(keys[0])
        answer = (3 * p) * (3 * (p ** 2)) * (3 * (p ** 3))
    } else if (freq === 2) {
        const p = Number(keys.find(k => dict[k] === 2));
        const q = Number(keys.find(k => dict[k] === 1));
        answer = (p * 2 + q) * (p ** 2 * 2 + q ** 2);
    } else {
        answer = Number(keys[0]) + Number(keys[1]) + Number(keys[2])
    }
    
    return answer;
}