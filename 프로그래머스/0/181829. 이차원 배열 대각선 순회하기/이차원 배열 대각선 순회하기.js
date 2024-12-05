function solution(board, k) {
    var answer = 0;
    
    const N = board.length
    const M = board[0].length
    
    for (let i=0; i < N; i++) {
        for (let j=0; j<M; j++) {
            if (i + j <= k) {
                answer += board[i][j]
            }
        }
    }
    
    return answer;
}