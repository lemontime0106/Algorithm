function solution(polynomial) {
    var answer = '';
    
    const array = polynomial.split(" + ");
    
    let x = 0;
    let y = 0;
    
    for (let arr of array) {
        if (arr.includes("x")) {
            if (arr === "x") {
                x++;
            } else {
                x += parseInt(arr.replace("x", ""));
            }
        } else {
            y += parseInt(arr);
        }
    }
    
    if (x > 0) {
        answer += x === 1 ? "x" : `${x}x`;
    }
    if (y > 0) {
        answer += x > 0 ? ` + ${y}` : `${y}`; 
    }
    
    return answer;
}
