function solution(code) {
    var ret = [];
    let mode = false;

    for (let i = 0; i < code.length; i++) {
        if (code[i] === "1") {
            mode = !mode;
        } else {
            if (!mode && i % 2 === 0) {
                ret.push(code[i]);
            } else if (mode && i % 2 === 1) {
                ret.push(code[i]);
            }
        }
    }
    
    if (!ret.length) {
        return "EMPTY"
    } else {
        return ret.join("")
    }
}