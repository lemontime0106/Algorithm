function solution(picture, k) {
    var answer = [];
    
    for (let i=0; i < picture.length; i++) {
        let temp = [];
        for (let j=0; j < picture[i].length; j++) {
            for (let r=0; r < k; r++) {
                temp.push(picture[i][j])
            }
        }
        
        for (let j=0; j < k; j++) {
            answer.push(temp.join(""))
        }
    }
    
    return answer;
}