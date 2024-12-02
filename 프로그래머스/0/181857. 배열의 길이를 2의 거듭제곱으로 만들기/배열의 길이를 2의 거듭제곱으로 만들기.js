function solution(arr) {
    var answer = arr;
    
    const total = arr.length;
    
    if (Number.isInteger(Math.log2(total))) {
        return arr;
    }
    
    const square = Math.pow(2, Math.ceil(Math.log2(total)))
    
    return [...arr, ...new Array(square - total).fill(0)];
}