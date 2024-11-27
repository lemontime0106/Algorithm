function solution(my_string, is_suffix) {
    var answer = 0;
    let word = [];

    for (let i = my_string.length - is_suffix.length; i < my_string.length; i++) {
        word.push(my_string[i]);
    }

    if (word.join('') === is_suffix) {
        answer = 1;
    }

    return answer;
}