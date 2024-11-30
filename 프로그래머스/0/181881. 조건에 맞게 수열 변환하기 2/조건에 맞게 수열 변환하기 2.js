function solution(arr) {
    let cnt = 0;
    let arr_prev = [...arr];

    while (true) {
        let arr_new = arr_prev.map((i) => {
            if (i % 2 === 0 && i >= 50) {
                return Math.floor(i / 2);
            } else if (i % 2 === 1 && i < 50) {
                return (i * 2) + 1;
            }
            return i;
        });

        if (arr_new.join('') === arr_prev.join('')) {
            break;
        }

        arr_prev = arr_new;
        cnt++;
    }

    return cnt;
}
