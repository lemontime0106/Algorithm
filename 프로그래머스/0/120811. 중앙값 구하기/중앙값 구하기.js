function solution(array) {
    array.sort((a, b) => a - b);
    
    const mid = Math.floor(array.length / 2);
    
    if (array.length % 2 === 0) {
        return (array[mid - 1] + array[mid]) / 2;
    } else {
        return array[mid];
    }
}