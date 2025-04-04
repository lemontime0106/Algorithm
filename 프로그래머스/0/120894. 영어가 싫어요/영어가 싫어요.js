function solution(numbers) {
    let answer = "";
    const dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    };

    let temp = "";
    for (let n of numbers) {
        temp += n;
        if (dict[temp]) {
            answer += dict[temp];
            temp = "";
        }
    }

    return parseInt(answer);
}
