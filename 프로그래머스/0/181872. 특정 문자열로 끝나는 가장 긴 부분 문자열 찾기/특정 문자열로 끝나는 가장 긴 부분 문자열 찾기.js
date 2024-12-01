function solution(myString, pat) {
    var answer = "";
    let temp = "";

    for (let i = 0; i < myString.length; i++) {
        temp += myString[i];

        if (temp.length >= pat.length) {
            let last = temp.slice(-pat.length);

            if (last === pat) {
                answer = temp;
            }
        }
    }

    return answer;
}