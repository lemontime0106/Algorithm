function solution(s) {
    let stack = [];
    let items = s.split(" ");

    for (let item of items) {
        if (item === "Z") {
            stack.pop();
        } else {
            stack.push(Number(item));
        }
    }

    return stack.reduce((acc, cur) => acc + cur, 0);
}