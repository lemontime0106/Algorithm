function solution(n) {
    const direct = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let answer = Array.from(Array(n), () => Array(n).fill(0));
    let x = 0, y = 0, dir = 0, num = 1;
    
    const isValid = (x, y) => {
        return x >= 0 && x < n && y >= 0 && y < n && answer[x][y] === 0;
    }
    
    while (num <= n ** 2) {
        answer[x][y] = num;
        let nextX = x + direct[dir][0];
        let nextY = y + direct[dir][1];
        if (!isValid(nextX, nextY)) {
            dir = (dir + 1) % 4;
            nextX = x + direct[dir][0];
            nextY = y + direct[dir][1];
        }
        x = nextX;
        y = nextY;
        num++;
    }
    
    return answer;
}