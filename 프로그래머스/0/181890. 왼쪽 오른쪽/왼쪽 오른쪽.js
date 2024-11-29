function solution(str_list) {
    var answer = [];
    
    let direct = "";
    let idx = -1;

    for (let i in str_list) {
        if (str_list[i] === "l" || str_list[i] === "r") {
            direct = str_list[i] === "l" ? "left" : "right";
            idx = Number(i);
            break;
        }
    }

    if (idx === -1) return [];

    if (direct === "left") {
        answer = str_list.slice(0, idx);
    } else if (direct === "right") {
        answer = str_list.slice(idx + 1);
    }

    return answer;
}
