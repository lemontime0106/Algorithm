function solution(my_string, s, e) {
    var answer = '';

    let head = '';
    let tail = '';
    let temp = [];

    for (let i = 0; i < s; i++) {
        head += my_string[i];
    }

    for (let i = e + 1; i < my_string.length; i++) {
        tail += my_string[i];
    }

    for (let i = e; i >= s; i--) {
        temp.push(my_string[i]);
    }

    answer = head + temp.join('') + tail;

    return answer;
}
