function solution(num, k) {
    let numStr = num.toString();
    let kStr = k.toString();      

    let index = numStr.indexOf(kStr);

    if (index === -1) {
        return -1;  
    } else {
        return index + 1;
    }
}
