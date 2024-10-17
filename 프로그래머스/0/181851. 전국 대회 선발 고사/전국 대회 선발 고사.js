function solution(rank, attendance) {
    var answer = 0;
    
    let student = []
    
    for (let i=0; i < rank.length; i++) {
        if (attendance[i]) {
            student.push([rank[i], i])
        }
    }
    
    student.sort((a, b) => a[0] - b[0]);
    student = student.slice(0, 3)
    
    answer = student[0][1] * 10000 + student[1][1] * 100 + student[2][1]
    
    return answer;
}