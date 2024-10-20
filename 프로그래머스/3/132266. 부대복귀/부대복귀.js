function solution(n, roads, sources, destination) {
    var answer = [];
    
    const MAP = Array.from({ length: n + 1 }, () => []);
    
    for (let road of roads) {
        let [a, b] = road;
        MAP[a].push(b);
        MAP[b].push(a);
    }
    
    let q = [destination];
    const visited = Array(n + 1).fill(-1);
    visited[destination] = 0;
    
    while (q.length) {
        let cur = q.shift();
        
        for (const next of MAP[cur]) {
            if (visited[next] === -1) { 
                q.push(next);
                visited[next] = visited[cur] + 1;
            }
        }
    }
    
    sources.forEach((s) => {
        answer.push(visited[s]);
    });
    
    return answer;
}
