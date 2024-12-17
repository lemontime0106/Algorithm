function solution(my_string) {
    let answer = 0;
    let temp = "";

    for (let i = 0; i < my_string.length; i++) {
        if (!isNaN(my_string[i]) && my_string[i] !== " ") {
            temp += my_string[i];
        } else {
            if (temp) {
                answer += Number(temp);
                temp = "";
            }
        }
    }

    if (temp) {
        answer += Number(temp);
    }

    return answer;
}
