function solution(arr) {
    var answer = [[]];
    
    const row = arr[0].length
    const col = arr.length
    
    if (row < col) {
        for (let i in arr) {
            while (arr[i].length < col) {
                arr[i].push(0)
            }
        }
    } else if (row > col) {
        for (let i = 0; i < (row - col); i++) {
            arr.push(new Array(row).fill(0))
        }
    }
    
    return arr;
}