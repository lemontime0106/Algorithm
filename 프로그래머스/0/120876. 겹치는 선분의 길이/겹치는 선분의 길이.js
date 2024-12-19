function solution(lines) {
    let segments = new Set();
    const N = lines.length;

    for (let i = 0; i < N; i++) {
        for (let j = i + 1; j < N; j++) {
            const start = Math.max(lines[i][0], lines[j][0]);
            const end = Math.min(lines[i][1], lines[j][1]);

            if (start < end) {
                for (let k = start; k < end; k++) {
                    segments.add(k);
                }
            }
        }
    }

    return segments.size;
}
