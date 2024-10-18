function solution(maps) {
    var answer = 1;
    const N = maps.length;
    const M = maps[0].length;
    const direct = [[-1, 0], [0, 1], [1, 0], [0, -1]];
    let visited = maps;
    let queue = [];
    
    queue.push([0, 0]);
    visited[0][0] = 0;
    
    while (queue.length > 0) {        
        let queueLength = queue.length;
        for (let i = 0; i < queueLength; i++) {
            let [x, y] = queue.shift();
            
            for (let j = 0; j < 4; j++) {
                let nx = x + direct[j][0];
                let ny = y + direct[j][1];
                
                if (nx >= 0 && nx < N && ny >= 0 && ny < M && visited[nx][ny] === 1) {
                    if (nx == N-1 && ny == M-1) {
                        return ++answer;
                    }
                    queue.push([nx, ny]);
                    visited[nx][ny] = 0;
                }
            }
        }
        answer++;
    }
    
    return -1;
}