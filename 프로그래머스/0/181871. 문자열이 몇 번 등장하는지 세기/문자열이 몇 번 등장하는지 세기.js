function solution(myString, pat) {
    var answer = 0;

    let start = 0;

    for (let i = 0; i <= myString.length - pat.length; i++) {
        if (myString.slice(start, start + pat.length) === pat) {
            answer++;
        }
        start++;
    }

    return answer;
}