function solution(board) {
    var answer = 0;
    
    const N = board.length;
    let MAP = Array.from({length: N}, () => Array(N).fill(0));
    
    const direct = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],         [0, 1],
        [1, -1], [1, 0], [1, 1]
    ];
    
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (board[i][j] === 1) {
                MAP[i][j] = 1;
                for (let [dx, dy] of direct) {
                    const nx = i + dx;
                    const ny = j + dy;
                    if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                        MAP[nx][ny] = 1;
                    }
                }
            }
        }
    }
    
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (MAP[i][j] === 0) {
                answer++;
            }
        }
    }
    
    return answer;
}