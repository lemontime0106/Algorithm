function solution(numbers) {
    numbers.sort((a, b) => a - b);

    const max = numbers[numbers.length - 1] * numbers[numbers.length - 2];
    const min = numbers[0] * numbers[1];

    return Math.max(max, min);
}
