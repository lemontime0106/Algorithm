function solution(array) {
    let dict = {};

    for (let a of array) {
        if (a in dict) {
            dict[a] += 1;
        } else {
            dict[a] = 1;
        }
    }

    let max = 0;
    let most = [];
    for (let num in dict) {
        if (dict[num] > max) {
            max = dict[num];
            most = [num];
        } else if (dict[num] === max) {
            most.push(num);
        }
    }

    if (most.length > 1) {
        return -1;
    }

    return parseInt(most[0]);
}
