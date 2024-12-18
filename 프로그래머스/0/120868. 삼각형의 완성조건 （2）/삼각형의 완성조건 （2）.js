function solution(sides) {
    const b = Math.max(...sides);
    const s = Math.min(...sides);
    
    const minPossible = b - s + 1;
    const maxPossible = b + s - 1;
    
    const answer = maxPossible - minPossible + 1;
    
    return answer;
}