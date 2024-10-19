function solution(maps) {
    const answer = [];
    const [X, Y] = [maps.length, maps[0].length];
    const visited = Array.from(Array(X), () => Array(Y).fill(false));
    const direct = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    
    const bfs = (a, b) => {
        let cnt = 0
        const q = [[a, b]];
        
        cnt += parseInt(maps[a][b]);
        visited[a][b] = true
        
        while (q.length > 0) {
            const [x, y] = q.shift()
            
            for (let d of direct) {
                const nx = x + d[0]
                const ny = y + d[1]
                if (nx >= 0 && nx < X && ny >= 0 && ny < Y && !visited[nx][ny] && maps[nx][ny] !== "X") {
                    visited[nx][ny] = true
                    cnt += parseInt(maps[nx][ny])
                    q.push([nx, ny])
                }
            }
        }
        answer.push(cnt);
    }
    
    for (let i=0; i < X; i++) {
        for (let j=0; j < Y; j++) {
            if (!visited[i][j] && maps[i][j] !== "X") {
                bfs(i, j)
            }
        }
    }
    
    if (answer.length === 0) {
        return [-1]
    } else {
        return answer.sort((a, b) => a - b);   
    }
}