function solution(dots) {
    function getSlope (a, b) {
        return (b[1] - a[1]) / (b[0] - a[0]);
    }
    
    const pair = [
        [0, 1, 2, 3],
        [0, 2, 1, 3],
        [0, 3, 1, 2]
    ]
    
    for (let [a1, b1, a2, b2] of pair) {
        const slope1 = getSlope(dots[a1], dots[b1])
        const slope2 = getSlope(dots[a2], dots[b2])
        
        if (slope1 === slope2) {
            return 1
        }
    }
    
    return 0;
}