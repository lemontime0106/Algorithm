function solution(myStr) {
    let result = [];
    let current = "";

    for (let char of myStr) {
        if (char === "a" || char === "b" || char === "c") {
            if (current.length > 0) {
                result.push(current);
                current = "";
            }
        } else {
            current += char;
        }
    }

    if (current.length > 0) {
        result.push(current);
    }

    return result.length > 0 ? result : ["EMPTY"];
}